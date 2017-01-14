# -*- coding: utf-8 -*-

import click
import meta_ultra.refs as refs
import meta_ultra.conf as conf
import meta_ultra.pipeline_runner as pipeline_runner

@click.group()
def main():
    pass

@main.command()
@click.option('--tool', prompt='TOOL', help='The tool that the reference is intended to be used with')
@click.option('--name', default=None, help='Reference Name')
@click.option('--ref', prompt='FILE PATH', help='Location of reference')
def add_reference(tool,name,ref):
    refs.add_reference(tool,name,ref)

@main.command()
def list_references():
    refs.list_references()

@main.command()
@click.option('--pairs/--single', default=False, help='Reads are pairwise')
@click.argument('samples', nargs=-1)
def new_conf(pairs,samples):
    conf.build_conf(samples,pairs=pairs)

@main.command()
@click.option('--dryrun/--normal',default=False,help='Print schedule but dont run anything')
@click.option('--jobs',default=1,help='Number of jobs to run')
@click.option('--conf',prompt='CONF FILE', help='Conf file, can be generated using \'pmp conf\'')
def run(dryrun,jobs,conf):
    pipeline_runner.run(conf,dry_run=dryrun,njobs=jobs)

if __name__ == "__main__":
    main()
