"""
@file
@brief Compute metrics in for a competition
"""
import os
import sys


if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def main_codalab_wrapper_binary_classification(fct, metric_name, argv, truth_file="truth.txt",
                                               submission_file="answer.txt", output_file="scores.txt"):
    """
    adapt the tempate available at
    `evaluate.py <https://github.com/Tivix/competition-examples/blob/master/hello_world/competition/scoring_program/evaluate.py>`_
    """
    input_dir = argv[1]
    output_dir = argv[2]

    submit_dir = os.path.join(input_dir, 'res')
    truth_dir = os.path.join(input_dir, 'ref')

    if not os.path.isdir(submit_dir):
        raise FileNotFoundError("%s doesn't exist" % submit_dir)

    if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        private_codalab_wrapper_binary_classification(fct, metric_name,
                                                      fold1=truth_dir, f1=truth_file,
                                                      fold2=submit_dir, f2=submission_file,
                                                      output=os.path.join(output_dir, output_file))
    else:
        raise FileNotFoundError(
            "{0} or {1} is not a folder".format(submit_dir, truth_dir))


def private_codalab_wrapper_binary_classification(fct, metric_name, fold1, fold2, f1="answer.txt", f2="answer.txt",
                                                  output="scores.txt", use_print=False):
    """
    Wraps the function following the guidelines
    `User_Building a Scoring Program for a Competition <https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition>`_.
    It replicates the example available at
    `competition-examples/hello_world <https://github.com/Tivix/competition-examples/tree/master/hello_world/competition>`_.

    @param      fct             function to wrap
    @param      metric_name     metric name
    @param      fold1           folder which contains the data for folder containing the truth
    @param      fold2           folder which contains the data for folder containing the data
    @param      f1              filename for the truth
    @param      f2              filename for the produced answers
    @param      output          produces an output with the expected results
    @param      use_print       display intermediate results
    @return                     metric
    """
    f1 = os.path.join(fold1, f1)
    f2 = os.path.join(fold2, f2)
    if not os.path.exists(f1):
        raise FileNotFoundError("unable to find '{0}'".format(f1))
    if not os.path.exists(f2):
        raise FileNotFoundError("unable to find '{0}'".format(f2))
    if f1 == f2:
        raise ValueError(
            "answers and scores are the same file: '{0}'".format(f1))

    with open(f1, "r") as f:
        lines = f.readlines()
    answers = [float(_) for _ in lines if _]
    if use_print:
        print("Reading answers:", f1, len(answers), "rows")
        print("First answers:", answers[:10])

    with open(f2, "r") as f:
        lines = f.readlines()
    scores = [float(_) for _ in lines if _]
    if use_print:
        print("Reading scores:", f1, len(scores), "rows")
        print("First scores:", scores[:10])

    metric = fct(answers, scores)
    res = "{0}:{1}".format(metric_name, metric)
    if use_print:
        print("Results=", res)
    with open(output, "w") as f:
        f.write(res)
    if use_print:
        print("Wrote", res, "in", output)
    return metric


def AUC(answers, scores):
    """
    Compute the `AUC <https://en.wikipedia.org/wiki/Area_under_the_curve_(pharmacokinetics)>`_.

    @param     answers      expected answers 0 (false), 1 (true)
    @param     scores       score obtained for class 1
    @return                 number
    """
    ab = list(zip(answers, scores))
    plus = [s for a, s in ab if a == 1]
    moins = [s for a, s in ab if a != 1]
    auc = 0
    for p in plus:
        for m in moins:
            if p > m:
                auc += 2
            elif p == m:
                auc += 1
    den = len(plus) * len(moins)
    if den == 0:
        return 1.0 if len(moins) == 0 else 0.0
    return auc * 1.0 / (len(plus) * len(moins) * 2)


def AUC_multi(answers, scores, ignored=None):
    """
    Compute the `AUC <https://en.wikipedia.org/wiki/Area_under_the_curve_(pharmacokinetics)>`_.

    @param      answers     expected answers `class` as a string
    @param      scores      prediction and score `(class, score)`
    @param      ignored     ignored class
    @return                 number
    """
    if ignored is None:
        ignored = []
    new_answers = [(1 if s[0] == a else 0)
                   for (a, s) in zip(answers, scores) if a not in ignored]
    return AUC(new_answers, scores)


def AUC_multi_multi(nb, answers, scores, ignored=None):
    """
    Compute the `AUC <https://en.wikipedia.org/wiki/Area_under_the_curve_(pharmacokinetics)>`_.

    @param      answers     expected answers, list of tuple of classes as a string
    @param      scores      prediction and score `(class, score)`
    @param      ignored     ignored class
    @return                 number

    Dummy expected classes (both classes):

    ::

        endettement	4.0
        surendettement	4.0
        surendettement	4.0
        surendettement	4.0

    Dummy predicted answers:

    ::

        2.0	endettement	0.48775936896183714	0.5033579692108108
        5.0	microcredit social	0.16592396695909017	0.8643847837801871
        5.0	microcredit personnel	0.7962830470795325	0.6233706526012659
        3.0	impayes	0.17370233487556486	0.779432954126955

    """
    res = []
    for i in range(0, nb):
        ta = [a[i] for a in answers]
        ts = [(a[i], a[nb + i]) for a in scores]
        auc = AUC_multi(ta, ts, ignored)
        err = sum(1 if a != s[0] else 0 for (a, s) in zip(ta, ts))
        res.append(err * 1.0 / len(ta))
        res.append(auc)
    return res


def private_codalab_wrapper_multi_classification(fct, variables_name, fold1, fold2, f1="answer.txt", f2="answer.txt",
                                                 output="scores.txt", use_print=False, ignored=None):
    """
    Wraps the function following the guidelines
    `User_Building a Scoring Program for a Competition <https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition>`_.
    It replicates the example available at
    `competition-examples/hello_world <https://github.com/Tivix/competition-examples/tree/master/hello_world/competition>`_.

    @param      fct             function to wrap
    @param      variables_name  variables names
    @param      fold1           folder which contains the data for folder containing the truth
    @param      fold2           folder which contains the data for folder containing the data
    @param      f1              filename for the truth
    @param      f2              filename for the produced answers
    @param      output          produces an output with the expected results
    @param      use_print       display intermediate results
    @param      ignored         ignored labels
    @return                     metric
    """
    f1 = os.path.join(fold1, f1)
    f2 = os.path.join(fold2, f2)
    if not os.path.exists(f1):
        raise FileNotFoundError("unable to find '{0}'".format(f1))
    if not os.path.exists(f2):
        raise FileNotFoundError("unable to find '{0}'".format(f2))
    if f1 == f2:
        raise ValueError(
            "answers and scores are the same file: '{0}'".format(f1))

    def pair_process(row):
        for i in range(len(row) // 2, len(row)):
            row[i] = float(row[i])
        return row

    with open(f1, "r") as f:
        lines = f.readlines()
    answers = [_.strip(" \r\n").split("\t") for _ in lines if _]

    if use_print:
        print("Reading answers:", f1, len(answers), "rows")
        print("First answers:", answers[:10])

    with open(f2, "r") as f:
        lines = f.readlines()

    scores = [pair_process(_.strip(" \r\n").split("\t")) for _ in lines if _]
    if use_print:
        print("Reading scores:", f1, len(scores), "rows")
        print("First scores:", scores[:10])

    metric = fct(len(variables_name), answers, scores, ignored=ignored)
    all_names = []
    for v in variables_name:
        all_names.append("%s_ERR" % v)
        all_names.append("%s_AUC" % v)

    res = "\n".join(["{0}:{1}".format(mn, m)
                     for (mn, m) in zip(all_names, metric)])
    if use_print:
        print("Results=", res)
    with open(output, "w") as f:
        f.write(res)
    if use_print:
        print("Wrote", res, "in", output)
    return metric


def main_codalab_wrapper_multi_classification(fct, variables_name, argv, truth_file="truth.txt",
                                              submission_file="answer.txt", output_file="scores.txt"):
    """
    adapt the tempate available at
    `evaluate.py <https://github.com/Tivix/competition-examples/blob/master/hello_world/competition/scoring_program/evaluate.py>`_
    """
    input_dir = argv[1]
    output_dir = argv[2]

    submit_dir = os.path.join(input_dir, 'res')
    truth_dir = os.path.join(input_dir, 'ref')

    if not os.path.isdir(submit_dir):
        raise FileNotFoundError("%s doesn't exist" % submit_dir)

    if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        private_codalab_wrapper_multi_classification(fct, variables_name,
                                                     fold1=truth_dir, f1=truth_file,
                                                     fold2=submit_dir, f2=submission_file,
                                                     output=os.path.join(
                                                         output_dir, output_file),
                                                     ignored=["nul"])
    else:
        raise FileNotFoundError(
            "{0} or {1} is not a folder".format(submit_dir, truth_dir))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("bad arguments: {0}".format(sys.argv))
    main_codalab_wrapper_multi_classification(AUC_multi_multi, ["orientation"], sys.argv)
