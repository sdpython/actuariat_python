#
# script to run for the first time
#
#
# specify a location by default
#

cat(".Rprofile: Setting UK repositoryn")
r = getOption("repos")
r["CRAN"] = "http://cran.uk.r-project.org"
options(repos = r)
rm(r)

#
# installation of others packages
#

install.packages(c('actuar',
                    'ADGofTest',
                    'AUC',
                    'CASdatasets',
                    'clusterGeneration',
                    'freeknotsplines',
                    'ggplot2',
                    'mnormt',
                    'RColorBrewer',
                    'rpart',
                    'splines',
                    'tm',
                    'xlsx',
                    'zoo'))

