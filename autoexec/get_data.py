# create a csv with data from the results
DIRECTORY_ROOT = "C:/ia-ap2"
actions = ['navigate', 'sample_soil', 'sample_rock', 'drop', 'calibrate', 'take_image', 'communicate_soil_data', 'communicate_rock_data', 'communicate_image_data']

# iterate a file line by line

def get_time(file):
  with open(file) as f:
    for line in f:
      if (line.startswith('Planning Time')):
        return (float(line.split(' ')[2].split('=')[1].split('sec')[0]))

def get_action_count(file):
    with open(file) as f:
      count = 0
      for line in f:
        if (line.startswith('(')):
          count+=1
      return count
 
    
def build_csv():
  results_dir = DIRECTORY_ROOT + "/autoexec/results"
  astar_dir = results_dir + "/astar"
  bfs_dir = results_dir + "/bfs"
  csv = "problem, astar_time, bfs_time, astar_actions, bfs_actions"
  for i in range(1, 21):
    try:
      v = "{:02d}".format(i)
      csv += "\n" + v + ", " + str(get_time(astar_dir + "/r" + v)) + ", " + str(get_time(bfs_dir + "/r" + v)) + ", " + str(get_action_count(astar_dir + "/r" + v)) + ", " + str(get_action_count(bfs_dir + "/r" + v))
    except:
      print("Error reading file " + v)
      continue

  with open(results_dir + "/results.csv", 'w') as f:
    f.write(csv)
    

if __name__ == "__main__":
  build_csv()