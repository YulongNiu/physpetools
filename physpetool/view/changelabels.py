# ########################## Copyrights and License ############################
#                                                                              #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                             #
#                                                                              #
# This file is part of Physpe.                                                 #
# https://xiaofeiyangyang.github.io/physpetools/                               #
#                                                                              #
# Physpe is free software: you can redistribute it and/or modify it under      #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# Physpe is distributed in the hope that it will be useful, but WITHOUT ANY    #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with Physpe. If not, see <http://www.gnu.org/licenses/>.               #
#                                                                              #
# ##############################################################################

"""
Change labels from abbreviation names to full names.
"""

from physpetool.database.dbpath import getlocaldbpath
from physpetool.utils.checkinputfile import checkFile, readIputFile
import os



dbpath = getlocaldbpath()


def taxlist():
    """
    prepare Taxonomy list
    :return: taxonomy list
    """
    orgpath = os.path.join(dbpath, "organism.txt")
    organism_list = []
    with open(orgpath) as f:
        for org in f:
            each_org = org.strip().split('\t')
            organism_list.append([each_org[1], each_org[2]])
    return organism_list


def annotatingLabels(input, output):
    """
Change labels
    :param input: input a files contain abb names
    :param output: output directory path
    :return: None
    """
    if not os.path.exists(output):
        os.makedirs(output)
    fw_name = "labels.txt"
    open_path = os.path.join(output, fw_name)
    fw = open(open_path, 'wb')
    fw.write('LABELS\nSEPARATOR TAB\nDATA\n')
    inputfile = checkFile(input)
    input_list = readIputFile(inputfile)
    tax_list = taxlist()
    for i in input_list:
        for j in tax_list:
            if i == j[0]:
                fw.write("{0}\t{1}\n".format(j[0], j[1]))
            else:
                pass
    fw.close()
    print("Change abbreviation names to full names complete")
    print("change labels file was save in {0}".format(open_path))