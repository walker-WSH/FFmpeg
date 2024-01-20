import os, shutil
 
root_dir = os.getcwd()+ os.sep+ ".."
print(root_dir)

dst_dir = root_dir + os.sep + "build" + os.sep + "pdb";
print(dst_dir)

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

print("------------------------------------------------")
if os.path.exists(root_dir):
    for dirnames, dirs, files in os.walk(root_dir):
        for filename in files:
            if not dirnames.startswith(dst_dir):
                if filename.endswith('.pdb') or filename.endswith('.PDB'):
                    old_path = dirnames + os.sep + filename;
                    new_path = dst_dir + os.sep + filename;
                    shutil.copyfile(old_path, new_path)
                    
                    print(old_path)
                    print(new_path)
                    print("")
                    
