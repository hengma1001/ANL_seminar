import __main__
__main__.pymol_argv = [ 'pymol', '-qc']
import pymol

pymol.finish_launching()
 


fspep_pdb = 'fs-peptide.pdb' 
pymol.cmd.load(fspep_pdb, 'fspep') 

fspep_pdb = 'low_RMSD.pdb'
pymol.cmd.load(fspep_pdb, 'lowRMSD') 

pymol.cmd.align('lowRMSD', 'fspep') 

pymol.cmd.zoom()
pymol.cmd.png('./model.png', 1920, 1280, dpi=300, ray=1) 
