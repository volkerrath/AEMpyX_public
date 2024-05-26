@REM Store AEMpyX env vars and set to this conda env
@REM so other AEMpyX installs don't pollute the environment

@set "AEMPYX_ROOT=C:\Users\33642\AEM"
@set "AEMPYX_DATA=C:\Users\33642\AEM\data"

conda create -n AEM -f AEMpyX_windows.txt
conda activate AEM
conda update --all

