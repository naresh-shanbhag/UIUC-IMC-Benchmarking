# Benchmarking In-memory Computing (IMC) Architectures
This is the repository for the database (Benchmarking_Data.csv) and Python code (plot_all.py) to generate annually updated versions of the plots found in our CICC'22 paper [Benchmarking In-memory Computing (IMC) Architectures](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9772817) which describes the benchmarking methodology. Please check for annual updates to the database which will occur sometime in August. Users are welcome to generate their own plots using our database. If you do so, please cite our paper and this GitHub repository. A BibTex code is provided below for those using LaTex.

Please inform us at [] of any errors in the database.

## About
In-memory computing (IMC) architectures have emerged as a compelling platform to implement energy efficient machine learning (ML) systems. However, today, the energy efficiency gains provided by IMC designs seem to be leveling off and it is not clear what the limiting factors are. The conceptual complexity of IMCs combined with the absence of a rigorous benchmarking methodology makes it difficult to gauge progress and identify bottlenecks in this exciting field. Our benchmarking methodology for IMCs comprises of: 1) a compositional view of IMCs that enables one to parse an IMC design into its canonical components; 2) a set of benchmarking metrics to quantify the performance, efficiency, and accuracy of IMCs; and 3) a strategy for analyzing the reported IMC data and metrics. We apply the proposed benchmarking methodology on an extensive database of IMC metrics extracted from > 70 IC designs published since 2018, in order to infer and comprehend trends in this area.

Our benchmarking effort indicates: 1) SRAM-based IMCs show a clear win in terms of energy efficiency and compute density over digital accelerators at the bank-level but the energy efficiency gap reduces dramatically when comparing at the processor level; 2) eNVM-based IMCs lag behind SRAM-based IMCs in terms of both energy efficiency and compute density, and surprisingly lag digital accelerators in terms of compute density; 3) the compute (bank-level) accuracy of IMCs, though a critical metric, is pervasively neglected in publications as is the energy vs. accuracy trade-off inherent to IMCs.

## Usage
Set the `OUTPUT_DIR` parameter on line 20 of `plot_all.py` to the output folder, and run
``` 
python3 plot_all.py
```
to plot all seven figures.

The `SAVE_PDF` and `SAVE_SVG` toggles determine which formats the plots are saved as. The `MARK_IMC_PROCESSOR`  controls whether each plot has IMC processors marked with red boxes.   

## Environment
The following Python 3 packages are required to run the program
* numpy
* matplotlib

## Citation
Please cite our paper and this GitHub repository if you use our benchmarking data.
```
@inproceedings{shanbhag2022comprehending,
  title={Comprehending In-memory Computing Trends via Proper Benchmarking},
  author={Shanbhag, Naresh R and Roy, Saion K},
  booktitle={2022 IEEE Custom Integrated Circuits Conference (CICC)},
  pages={01--07},
  year={2022},
  organization={IEEE}
}
```
