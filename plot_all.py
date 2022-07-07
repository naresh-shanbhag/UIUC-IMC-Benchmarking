#################################################################################
# Han-Mo Ou 070722
# Python Plots
#################################################################################

import csv 
import numpy as np
from matplotlib import pyplot as plt

# Set Output Directory
OUTPUT_DIR = 'Figures_Test'

# Empty Class to Store Data
class Data: 
    pass

def fetch_data():
    with open('Benchmarking_Data.csv') as file:
        # Load CSV File
        reader = list(csv.DictReader(file)) 
        for row in reader:
            for key in row:
                if row[key] == '':
                    row[key] = float('NAN')
                    
        data = Data()

        # Converting CSV Data to Array
        data.TOPS_mm2     = np.array([row['TOPS/mm2'] for row in reader], dtype = np.float32)
        data.TOPS_W       = np.array([row['TOPS/W'] for row in reader], dtype = np.float32)
        data.B_pre_ADC    = np.array([row['B_pre-ADC'] for row in reader], dtype = np.float32)
        data.Tech         = np.array([row['Tech (nm)'] for row in reader], dtype = np.int32)
        data.Year         = np.array([row['Year'] for row in reader], dtype = np.float32)
        data.core_size    = np.array([row['Core Size(Kb)'] for row in reader], dtype = np.float32)
        data.N_row        = np.array([row['N_row'] for row in reader], dtype = np.float32)
        data.N_col        = np.array([row['N_col'] for row in reader], dtype = np.float32)
        data.Vdd          = np.array([row['Supply V(V)'] for row in reader])
        data.B_X          = np.array([row['B_x'] for row in reader], dtype = np.float32)
        data.B_W          = np.array([row['B_w'] for row in reader], dtype = np.float32)
        data.B_ADC        = np.array([row['B_ADC'] for row in reader], dtype = np.float32)
        data.R_C          = np.array([row['R_C'] for row in reader], dtype = np.float32)
        data.R            = np.array([row['R'] for row in reader], dtype = np.float32)
        data.C_C          = np.array([row['C_C'] for row in reader], dtype = np.float32)
        data.C            = np.array([row['C'] for row in reader], dtype = np.float32)
        data.N_ADC        = np.array([row['N_ADC'] for row in reader], dtype = np.float32)
        data.N            = np.array([row['N'] for row in reader], dtype = np.float32)
        data.N_1b         = np.array([row['N_1b'] for row in reader], dtype = np.float32)
        data.B_core       = np.array([row['B_core'] for row in reader], dtype = np.float32)
        data.alpha        = np.array([row['alpha'] for row in reader], dtype = np.float32)
        data.B_col        = data.B_X * data.R_C * data.C_C
        data.T_core_ns    = np.array([row['T_core(ns)'] for row in reader], dtype = np.float32)
        data.E_OP1_fJ     = np.array([row['E_OP1 (fJ)'] for row in reader], dtype = np.float32)
        data.N_core       = np.array([row['N_core'] for row in reader], dtype = np.float32)
        data.E_col_fJ     = np.array([row['E_col (fJ)'] for row in reader], dtype = np.float32)
        data.E_core_pJ    = np.array([row['E_core (pJ)'] for row in reader], dtype = np.float32)
        data.E_mvm_pJ     = np.array([row['E_mvm (pJ)'] for row in reader], dtype = np.float32)
        data.Cell_Type    = [row['Cell Type'] for row in reader]
        data.Compute_Mod  = [row['Compute Model'] for row in reader]
        data.Arch         = [row['Architecture'] for row in reader]
        data.TOPS_a       = np.array([row['TOPS_a '] for row in reader], dtype = np.float32)
        data.TOPS         = np.array([row['TOPS'] for row in reader], dtype = np.float32)
        

    return data

TECH_LIST = [5,7,12,16,22,28,45,55,65,180]

# SRAM: TOPS/W vs. TOPS/mm^2 (with TSMC paper)
def plot_1(data): 
    
    fig, ax = plt.subplots(figsize = (9,7))
    
    colors = 'rrggbbcckk'
    marker = 'ososososos'
    marker_size = 100 
    
    for j, t in enumerate(TECH_LIST):
        SRAM = np.array( [i for i in range(len(data.Arch)) if  data.Arch[i] == 'SRAM' and data.Tech[i] == t])
        ax.scatter(data.TOPS_mm2[SRAM], data.TOPS_W[SRAM], marker_size, colors[j], marker[j], label = '%dnm'%t)
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(which = 'both')
    
    ax.legend(fontsize = 12)
    ax.set_title('Energy-efficiency vs. Compute Density', fontsize = 15)
    ax.set_xlabel('1b-TOPS/mm$^2$', fontsize = 15)
    ax.set_ylabel('1b-TOPS/W', fontsize = 15)

    fig.savefig(OUTPUT_DIR + '/1_1b-TOPSpW_vs_1bTOPSpmm2_SRAM.svg')
    fig.savefig(OUTPUT_DIR + '/1_1b-TOPSpW_vs_1bTOPSpmm2_SRAM.pdf')


# SRAM: TOPS/W vs. TOPS
def plot_2(data):
    fig, ax = plt.subplots(figsize = (9,7))
    
    colors = 'rrggbbcckk'
    marker = 'ososososos'
    marker_size = 100 
    
    for j, t in enumerate(TECH_LIST):
        SRAM = np.array( [i for i in range(len(data.Arch)) if  data.Arch[i] == 'SRAM' and data.Tech[i] == t])
        ax.scatter(data.TOPS[SRAM], data.TOPS_W[SRAM], marker_size, colors[j], marker[j], label = '%dnm'%t)
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(which = 'both')
    
    ax.legend(fontsize = 12)
    ax.set_title('Energy Efficiency vs. Throughput', fontsize = 15)
    ax.set_xlabel('1b-TOPS', fontsize = 15)
    ax.set_ylabel('1b-TOPS/W', fontsize = 15)

    fig.savefig(OUTPUT_DIR + '/2_1b-TOPSpW_vs_1b-TOPS_SRAM.svg')
    fig.savefig(OUTPUT_DIR + '/2_1b-TOPSpW_vs_1b-TOPS_SRAM.pdf')


# SRAM: TOPS/W vs. B_I_col
def plot_3(data):
    fig, ax = plt.subplots(figsize = (9,7))
    
    colors = 'rrggbbcckk'
    marker = 'ososososos'
    marker_size = 100 
    
    for j, t in enumerate(TECH_LIST):
        SRAM = np.array( [i for i in range(len(data.Arch)) if  data.Arch[i] == 'SRAM' and data.Tech[i] == t])
        ax.scatter(data.B_pre_ADC[SRAM], data.TOPS_W[SRAM], marker_size, colors[j], marker[j], label = '%dnm'%t)
    
    ax.set_yscale('log')
    ax.grid(which = 'both')
    
    ax.legend(fontsize = 12)
    ax.set_title('Energy-efficiency vs. Pre-ADC Information Content', fontsize = 15)
    ax.set_xlabel('$B_{I(col)}$ (bits)', fontsize = 15)
    ax.set_ylabel('1b-TOPS/W', fontsize = 15)

    fig.savefig(OUTPUT_DIR + '/3_1b-TOPSpW_vs_BIcol_SRAM.svg')
    fig.savefig(OUTPUT_DIR + '/3_1b-TOPSpW_vs_BIcol_SRAM.pdf')


# SRAM: B_ADC vs. B_pre_ADC
def plot_4(data):
    fig, ax = plt.subplots(figsize = (9,7))
    
    colors = 'rrggbbcckk'
    marker = 'ososososos'
    marker_size = 100 
    
    for j, t in enumerate(TECH_LIST):
        SRAM = np.array( [i for i in range(len(data.Arch)) if  data.Arch[i] == 'SRAM' and data.Tech[i] == t])
        ax.scatter(data.B_pre_ADC[SRAM], data.B_ADC[SRAM], marker_size, colors[j], marker[j], label = '%dnm'%t)
    
    ax.grid(which = 'both')
    
    ax.legend(fontsize = 12)
    ax.set_title('ADC Precision vs. Pre-ADC Information Content', fontsize = 15)
    ax.set_xlabel('$B_{I(col)}$ (bits)', fontsize = 15)
    ax.set_ylabel('$B_{ADC}$ (bits)', fontsize = 15)

    fig.savefig(OUTPUT_DIR + '/4_BADC_vs_BIcol_SRAM.svg')
    fig.savefig(OUTPUT_DIR + '/4_BADC_vs_BIcol_SRAM.pdf')
    
def plot_5(data):
    pass
    
def plot_6(data):
    pass
    
def plot_7(data):
    pass
    
    
def main():
    data = fetch_data()
    plot_1(data)
    plot_2(data)
    plot_3(data)
    plot_4(data)

if __name__ == '__main__':
    main()
