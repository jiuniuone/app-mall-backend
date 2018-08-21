#!/bin/bash
logDir='/var/log/mall'

doArchieve()
{
    logFile=$logDir/$1.log
    d=`date -d "yesterday" +%Y%m%d`
    targetFile=$logDir/$1-${d}.log
    echo $targetFile
    cp $logFile $targetFile
    echo "" > $logFile
    gzip $targetFile

}

doArchieve mall