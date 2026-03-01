import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def generate_figure_6_1():
    """
    Reproduces Figure 6.1: The Energy Chasm.
    """
    duration = np.linspace(0, 14, 100)
    # 15.6 TWh at 10 days -> 1.56 TWh/day
    energy_gap_legacy = 1.56 * duration
    # MCP flexibility reduces gap by 60-70%
    energy_gap_mcp = 0.4 * energy_gap_legacy
    
    plt.figure(figsize=(10, 6))
    plt.plot(duration, energy_gap_legacy, 'r-', label='Physical Energy Gap (Legacy)')
    plt.plot(duration, energy_gap_mcp, 'b-', label='MCP-Enabled Flexibility (Virtual Storage)')
    plt.fill_between(duration, energy_gap_mcp, energy_gap_legacy, color='blue', alpha=0.1, label='Protocol Dividend')
    
    plt.axhline(y=0.07, color='k', linestyle='--', label='2026 Storage Limit (0.07 TWh)')
    
    plt.title('Figure 6.1: The Energy Chasm')
    plt.xlabel('Dunkelflaute Duration (Days)')
    plt.ylabel('Energy Gap (TWh)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/figure_6_1.png')
    plt.close()

def generate_figure_6_2():
    """
    Reproduces Figure 6.2: The Redispatch Cliff.
    """
    years = np.arange(2020, 2031)
    legacy_trend = np.array([1.2, 1.5, 2.3, 2.8, 3.1, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
    mcp_trend = np.array([1.2, 1.5, 2.3, 2.8, 3.1, 2.8, 2.2, 1.8, 1.4, 1.1, 0.9])
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, legacy_trend, 'r-o', label='Manual Redispatch (Legacy)')
    plt.plot(years, mcp_trend, 'b-o', label='MCP-Enabled Balancing (2030 Roadmap)')
    
    plt.axvline(x=2026, color='k', linestyle='--', label='The Protocol Pivot (2026)')
    
    plt.title('Figure 6.2: The Redispatch Cliff')
    plt.xlabel('Year')
    plt.ylabel('Redispatch Cost (€ Billion)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/figure_6_2.png')
    plt.close()

if __name__ == "__main__":
    os.makedirs('plots', exist_ok=True)
    generate_figure_6_1()
    generate_figure_6_2()
    print("Figures 6.1 and 6.2 generated successfully in plots/ directory.")
