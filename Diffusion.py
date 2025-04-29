import numpy as N

__author__ = 'v-caearl'

COLD = 0
AMBIENT = 25
HOT = 50

def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    return(1-8*diffusionRate)*site + diffusionRate*(N + NE + E +  SE + S + SW + W + NW)

def initBar(m, n, hotSites, coldSites):
    ambientBar = [[AMBIENT for _ in range(n)] for _ in range(m)]
    for r, c in hotSites:
        ambientBar[r][c] = HOT
    for r, c in coldSites:
        ambientBar[r][c] = COLD

    return ambientBar

def applyHotCold(bar, hotSites, coldSites):
    for r, c in hotSites:
        bar[r][c] = HOT
    for r, c in coldSites:
        bar[r][c] = COLD

    return bar 

def reflectingLat(lat):
    # Duping top and bottom rows
    topRow = lat[0][:]
    bottomRow = lat[-1][:]
    latNS = [topRow] + lat + [bottomRow]
    
    # Duping left and right columns of lat
    extended_lat = []
    for row in latNS:
        left = row[0]
        right = row[-1]
        new_row = [left] + row + [right]
        extended_lat.append(new_row)
    
    return extended_lat

def applyDiffusionExtended(diffusionRate, bar):
    

def diffusionSim(m, n, diffusionRate, t):
    bar = initBar(m, n, )
    grids = []
    for _ in range(1, t + 1):
        barExtended = reflectingLat(bar)
        bar = applyDiffusionExtended(diffusionRate, barExtended)
        bar = applyHotCold(bar, hotSites, coldSites)
        grids.append(bar)
    return grids