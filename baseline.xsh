#!/usr/bin/env xonsh
''' Matain the history baseline. '''
$RAISE_SUBPROC_ERROR = True

import config
from baseline_strategy import GitStrategy

strategy = GitStrategy(config.baseline_repo_url(), config.baseline_local_repo_path())
