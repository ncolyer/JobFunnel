#!python
"""Builds a config from CLI, runs desired scrapers and updates JSON + CSV
"""
import sys
from .backend.jobfunnel import JobFunnel
from .config import parse_cli, build_config_dict, get_config_manager


def main():
    """Parse CLI and call jobfunnel() to manage scrapers and lists
    """
    # Parse CLI into validated schema
    args = parse_cli(sys.argv[1:])
    cfg_dict = build_config_dict(args)

    # Build config manager
    funnel_cfg = get_config_manager(cfg_dict)
    funnel_cfg.create_dirs()

    # Init
    job_funnel = JobFunnel(funnel_cfg)

    # Run or recover
    if args['do_recovery_mode']:
        job_funnel.recover()
    else:
        job_funnel.run()


if __name__ == '__main__':
    main()
