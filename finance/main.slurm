#!/bin/sh
#SBATCH --job-name compfinance         # this is a parameter to help you sort your job when listing it
#SBATCH --error run.e%j     # optional. By default a file slurm-{jobid}.out will be created
#SBATCH --output run.o%j      # optional. By default the error and output files are merged
#SBATCH --ntasks 1                    # number of tasks in your job. One by default
#SBATCH --cpus-per-task 4             # number of cpus for each task. One by default
#SBATCH --mem 8                   #####CPU is mutually exclusive with the one for GPUs.#sbatch --mem-per-cpu=16000 # in MB
#SBATCH --partition debug-cpu         # the partition to use. By default debug-cpu. (shared-gpu)
#SBATCH --gres=gpu:0, #VramPerGpu:12G
#SBATCH --time 0-00:14:59                  # maximum run time.
# module load my sosftware               # load a specific software using module, for example Python


## USATO Python 3.8.18
module load Anaconda3
eval "$(conda shell.bash hook)"
conda activate test_gpu
###################################

python -u code/tp01/main.py



# sbatch --gpus=ampere:1
