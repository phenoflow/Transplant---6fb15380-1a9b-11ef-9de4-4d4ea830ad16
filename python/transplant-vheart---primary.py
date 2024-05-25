# Sara Muller, Samantha L Hider, Karim Raza, Rebecca J Stack, Richard A Hayward, Christian D Mallen, 2024.

import sys, csv, re

codes = [{"code":"7901000","system":"readv2"},{"code":"7901z00","system":"readv2"},{"code":"TB00000","system":"readv2"},{"code":"7900z00","system":"readv2"},{"code":"7901y00","system":"readv2"},{"code":"7900","system":"readv2"},{"code":"7901100","system":"readv2"},{"code":"7901500","system":"readv2"},{"code":"SP08400","system":"readv2"},{"code":"7B00400","system":"readv2"},{"code":"7901","system":"readv2"},{"code":"7901300","system":"readv2"},{"code":"7900000","system":"readv2"},{"code":"ZV59600","system":"readv2"},{"code":"ZV42100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('transplant-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["transplant-vheart---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["transplant-vheart---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["transplant-vheart---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
