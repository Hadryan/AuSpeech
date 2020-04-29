import os, json
from wav2vec import WavDecoder

master_list = {}
part_number = 1

for i, file in enumerate(os.listdir("MELD.Raw/test_wav")):
  if i > 0 and i % 100 == 0:
    json.dump(master_list, open("json_parts_test/part{}.json".format(part_number), "w"))
    part_number += 1
    master_list = {}
    print("Part written")
  
  wd = WavDecoder(os.path.join("wav", file))
  frames = []
  for f in wd:
      frames.append(f)
  ys = [p.y for p in frames[0][0]]
  master_list[file.split(".")[0]] = ys[:10000]
  if i % 100 == 0:
    print("{} done".format(i))
