
import subprocess as sp
import meta_ultra.config as config

def run(conf,njobs=1,dry_run=False):
    
    cmd = 'snakemake --snakefile {snkf} --jobs {njobs} --configfile {conf}'
    cmd = cmd.format(snkf=config.snake_file,
                     njobs=njobs,
                     conf=conf
                     )
    if dry_run:
        cmd += ' --dryrun'
    sp.call(cmd,shell=True)
    
