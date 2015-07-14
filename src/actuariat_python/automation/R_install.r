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
                    'AMORE',
                    'arules',
                    'arulesViz',
                    'ADGofTest',
                    'AUC',
                    'CASdatasets',
                    'clusterGeneration',
                    'extraTrees',
                    'freeknotsplines',
                    'ggplot2',
                    'HadoopStreaming',
                    'h2o',
                    'kohonen',
                    'mnormt',
                    'monmlp',
                    'nza',
                    'plyrmr',
                    'RBGL',
                    'RColorBrewer',
                    'RevoScaleR',
                    'Rfacebook',
                    'RHadoop',
                    'rhbase',
                    'rhdfs',
                    'RHIPE',
                    'rmr2',
                    'RSNNS',
                    'rpart',
                    'shglm',
                    'sna',
                    'SnowballC',
                    'som',
                    'splines',
                    'TeachingDemos',
                    'tm',
                    'twitteR',                    
                    'xlsx',
                    'zoo'))
                    
install.packages("foreach")
install.packages("doMC")
install.packages("Matrix")
install.packages("glmnet")
install.packages("kernlab")
install.packages("e1071")
install.packages("gbm")
install.packages("randomForest")                    
                    
#
# Spark
# 

install.packages(c('rJava',
                   'testthat'))
  
# does not compile                   
# see https://groups.google.com/forum/#!topic/sparkr-dev/Yss1ViIfBYo
# library(devtools)
# library(rJava)
# install_github("amplab-extras/SparkR-pkg", subdir="pkg")


