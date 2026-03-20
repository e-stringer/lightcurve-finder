# lightcurve-finder
Script with GUI to quickly query ZTF, Gaia, ASAS-SN, and TESS and check for variability



Installation
  * It's recommended to create a new conda environment with python 3.12:
    -> conda create -n lightcurve-finder python=3.12
  * Activate your conda environment by running:
    -> conda activate lightcurve-finder
  * Navigate to the folder in which you wish to install the software
  * Download the files by running:
    -> git clone git@github.com:e-stringer/lightcurve-finder.git
  * Navigate into the folder titled "lightcurve-finder"
  * Install the dependencies with:
    -> pip install -e .

Usage:
  * The software can be run by typing:
    -> lightcurve-finder

Functions:
  * Survey: A dropdown menu to select the survey you'd like to query. Note: you will need a free IRSA account to query ZTF. The credentials     are only requested the first time you query. You can make an account by following the link below:
      - https://irsa.ipac.caltech.edu/frontpage/
  * RA/DEC: The coordinates of your target. Accepts both decimal degrees and sexagesimal.
  * Radius: Cone search radius of your coordinates in arcseconds. Right now the software can't handle multiple objects appearing in the         search, so try to avoid that by using a small radius.
  * Plot alpha: Transparency level of the points on your plots. If you happen to get very high cadence data (like in TESS) this can help        you in seeing any variablility.
  * Band: A dropdown menu to select the photometric band you would like to analyze with Lomb Scargle.
  * Min Freq. (c/d)/Max Freq. (c/d): The frequency range in cycles/day to be used in the Lomb Scargle analysis. Can be switched into period     space in days, hours, or minutes. The numbers in the text-box will dynamically change to match the selected units. The Lomb Scargle         plot will be displayed in the units selected in the top box.
  * niters: The number of frequency steps between your maximum and minimum for the Lomb Scargle analysis. This is combined with your min/       max gives you your frequency resolution. Increasing this linearly increases the time it takes the Lomb Scargle to run, so 1e6 will take     10 times longer than 1e5. I recommend decreasing the frequency range rather than increasing niters, if at all possible.
  * nterms: This is the number of terms in the fourier transform (e.g. nterms=1 is a sine fit). For sinusoidal variation nterms=1 is            best, but more complicated shapes (triangle waves, sawtooth) are more precisely fit with more terms. More terms makes the lomb-scargle      take longer. I wouldn't go over 4-5 terms.
  * Save Data: Click to save the photometry from the last survey you queried. Everything is saved in .csv format. A window will appear that     lets you select the columns you would like to save. You can also separate the data by band, and save each band to its own file. To do       this, check the box at the top that says "save bands to separate files". Click OK and a standard save prompt will appear. If you are        saving each band to it's own file, a suffix will be added to whatever you put in for the name (e.g. if you put "ztf_star" it will save      as "ztf_star_g.csv", "ztf_star_r.csv", and "ztf_star_i.csv").
  * Query: Queries the selected survey using a cone search, and plots each band. For Gaia, the object will also be plotted on an HR             diagram. The HR diagram is reddening corrected, but the object is not. Warning: queries can often get stuck due to their database being     down for mainenance. For right now, use ctrl-c in the terminal to kill the query if it takes too long. Queries shouldn't normally take      more than a minute or so.
  * Lomb Scargle: Runs a Lomb Scargle periodogram using the parameters on the right-hand side of the window (see above). Will output a          power-frequency diagram, as well as the photometry in your selected band folded over that frequency.
  * Replot: Simply replots the photometry and Lomb Scargle plots of your most recently queried survey. This will not re-query or re-run the     Lomb Scargle. If your last query was Gaia, it will also replot the HR diagram. This exists just to allow you to quickly re-open a plot      without having to re-run anything. Will detect and use a new Plot alpha value, so it is also useful for adjusting that.
