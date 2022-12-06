import subprocess
import sys

DIRECTORY_ROOT = "C:/ia-ap2"

RESULTS_DIR = DIRECTORY_ROOT + "/autoexec/results"
BACKUP_RESULTS_DIR = DIRECTORY_ROOT + "/autoexec/backup_results"
JARS_DIR = DIRECTORY_ROOT + "/jars"

PROBLEMS_PATH = DIRECTORY_ROOT + "/problems/rovers"
DOMAIN_PATH = PROBLEMS_PATH + "/domain.pddl"

#ASTAR_PATH = JARS_DIR + "/astar.jar"
#BFS_PATH = JARS_DIR + "/bfs.jar"

TIMEOUT_TIME = 60 * 10 # 5 minutes

ENV = '/usr/bin/env'
JAVA_EXEC = "C:/Program Files/Amazon Corretto/jdk1.8.0_342/bin/java.exe"
BIN = 'C:/ia-ap2/bin'
MAIN_FILE = "javaff.JavaFF"

command_arr = ['timeout', str(TIMEOUT_TIME), ENV, JAVA_EXEC, '-cp', BIN, MAIN_FILE]

def execute_problem(algorithm):
  print('Executing tests in ' + algorithm)
  res = bytes()

  for i in range(1, 21):
    directory = RESULTS_DIR + "/astar/r" if algorithm == "astar" else RESULTS_DIR + "/bfs/r"

    # sometimes it doesnt print the results, but we need the time
    backup_dir = BACKUP_RESULTS_DIR + "/astar/r" if algorithm == "astar" else BACKUP_RESULTS_DIR + "/bfs/r" 

    v = "{:02d}".format(i)
    print("\nExecuting problem " + v)
    command = command_arr + [DOMAIN_PATH, PROBLEMS_PATH + '/pfile' + v, '10', backup_dir + v, algorithm]
    print(' '.join(command)) 
    try:
      res = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
      print("\nError executing problem " + v + ": " + str(e))
      # keep going
      continue

    # write results to file
    with open(directory + v, 'w') as f:
      f.write(res.decode('utf-8'))




if __name__ == "__main__":
    # get command line arguments
    option = sys.argv[1]
    if option == "astar":
        execute_problem("astar")
    elif option == "bfs":
        execute_problem("bfs")
    else:
        print("Invalid option")