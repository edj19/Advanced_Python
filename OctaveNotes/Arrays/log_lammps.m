%------------Read lammps Log File-------------------
fileID = fopen('log.lammps','r');
line = fgetl(fileID);
while ischar(line)
##  disp(line)
  if line(1:4)=="Step"
    disp(line)
  end
  line=fgetl(fileID);
endwhile

fclose(fileID);
