# Glucometer
 Extracting Blood Sugar
The new generation of wearable devices allow patients with diabetes mellitus to be continuously monitored and non-invasive blood sugar. The values ​​of the individual devices are sent on a daily basis to a data center which assembles a single file containing the data of all patients connected to the monitoring service. You want create a program capable of extracting some statistics. Specifically, a check on the exceeding the maximum level of 200mg/dL.

Technical specifications follow.

The program has to manage a glucometers.txt input file containing the data of a whole day of measurement. This file must be understood as an aggregate of the data collected and therefore containing, in no particular order, the data of all patients.

Data for a single patient is in chronological order and missing measurements may occur (intervals in which the patient is not wearing the device).

All measurements are made on a regular basis: one sample every 5 minutes.

Each line of the file contains 5 different data separated by a single space and in the following order:

patient identification code consisting of 4 hexadecimal characters (PPPP format);
acquisition time (hh:mm format)
blood glucose value (g)
body temperature (°C)
heart rate (bpm).
The program, after storing the data in an appropriate data structure, will have to print the list of all the patients who have recorded at least one exceedance and, for each exceedance, the time and blood glucose level corresponding. The list must appear in order of criticality, starting with the patient with the most exceedances