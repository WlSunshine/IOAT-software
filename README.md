# IOAT-software
An interactive tool for statistical analysis and visualization of omics data and clinical data



                                                                           USER MANUAL FOR IOAT 
Chapter 1. Software Overview

This system is a data analysis tool based on machine learning. In multi-omics data using bioinformatics, the clinical data survival time and survival status of multi-omics data can be combined with multiple omics data such as gene expression data , Methylated data, copy number combination, pre-processing data through relevant machine learning methods, feature screening, clustering the filtered features to use the clustered results as the true labels of data for survival analysis. 
 
Chapter 2. Installation

The chapter explains how to download and install IOAT on the user’s computer.

2.1 Requirement

1)	Hardware requirements

a)	Intel Pentium III/800 MHz or higher (or compatible) although one should probably not go below a dual core processor.
b)	2 GB RAM minimum.
2)	Software requirements

a)	Supported operating system (OS) versions (32-bit or 64-bit)
Windows 7 SP1
Windows Server 2008 R2 SP1
Windows Server 2008 SP2
Windows Server 2012 R2
Windows 8
Windows 10
b)	Python v3.5.6 (for Windows) .
c)	R v3.5.1 (for Windows) .

2.2 Configuration of Environment

2.2.1 Installing R-3.5.1-win.exe

Users should install R-3.5.1-win.exe of these IOAT-software before starting IOAT. After installing R-3.5.1-win.exe, the user needs to configure the environment R variables.

2.2.2 Installing mainUI.exe of python

After installing R-3.5.1-win.exe, the user needs to execute IOAT.exe in the dist file to run the IOAT tool. 

2.3 Download

IOAT can be freely downloaded from https://pan.baidu.com/s/1qD6mUQBquSQPyfJtudqR5A ,
password:xkwm. Compress the zip package (or 7z) into a specified file folder.

2.4 Data Format

This tool is mainly for data in CSV format, and requires the input data format to be in the first column of data with a label of 'time', which is the patient's survival time; the second column of data with a label of 'status', which is the patient's survival status; the next is multi-omics feature fusion data.




