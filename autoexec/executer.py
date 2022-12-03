import subprocess
import sys

DIRECTORY_ROOT = "C:/ia-ap2"

RESULTS_DIR = DIRECTORY_ROOT + "/autoexec/results"
JARS_DIR = DIRECTORY_ROOT + "/jars"

PROBLEMS_PATH = DIRECTORY_ROOT + "/problems/rovers"
DOMAIN_PATH = PROBLEMS_PATH + "/domain.pddl"

ASTAR_PATH = JARS_DIR + "/astar.jar"
BFS_PATH = JARS_DIR + "/bfs.jar"

TIMEOUT_TIME = 60 * 10 # 5 minutes
command_arr = ['timeout', str(TIMEOUT_TIME), 'java', '-jar']

def execute_problem(jarPath):

  for i in range(1, 20):
    v = "{:02d}".format(i)
    print("\nExecuting problem " + v)
    command = command_arr + [ASTAR_PATH, DOMAIN_PATH, PROBLEMS_PATH + '/pfile' + v]
    try:
      res = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
      print("\nError executing problem " + v + ": " + str(e))
      # keep going
      continue
    # put res in a file
    dir = RESULTS_DIR + "/astar/r" if jarPath == ASTAR_PATH else RESULTS_DIR + "/bfs/r"
    with open(dir + v , 'w') as f:
      print('\nWriting results for problem ' + v)
      f.write(bytes.decode(res, 'utf-8'))

if __name__ == "__main__":
    # get command line arguments
    option = sys.argv[1]
    if option == "astar":
        execute_problem(ASTAR_PATH)
    elif option == "bfs":
        execute_problem(BFS_PATH)
    else:
        print("Invalid option")