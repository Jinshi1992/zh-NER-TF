import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    PER = get_PER_entity(tag_seq, char_seq)
    LOC = get_LOC_entity(tag_seq, char_seq)
    ORG = get_ORG_entity(tag_seq, char_seq)
    ORG = get_OTH_entity(tag_seq, char_seq)
    #MISC = get_MISC_entity(tag_seq, char_seq)
    return PER, LOC, ORG, OTH#, MISC


def get_PER_entity(tag_seq, char_seq):
    length = len(char_seq)
    PER = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-PER':
            if 'per' in locals().keys():
                PER.append(per)
                del per
            per = char
            if i+1 == length:
                PER.append(per)
        if tag == 'I-PER':
            per += char
            if i+1 == length:
                PER.append(per)
        if tag not in ['I-PER', 'B-PER']:
            if 'per' in locals().keys():
                PER.append(per)
                del per
            continue
    return PER


def get_LOC_entity(tag_seq, char_seq):
    length = len(char_seq)
    LOC = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-LOC':
            if 'loc' in locals().keys():
                LOC.append(loc)
                del loc
            loc = char
            if i+1 == length:
                LOC.append(loc)
        if tag == 'I-LOC':
            loc += char
            if i+1 == length:
                LOC.append(loc)
        if tag not in ['I-LOC', 'B-LOC']:
            if 'loc' in locals().keys():
                LOC.append(loc)
                del loc
            continue
    return LOC


def get_ORG_entity(tag_seq, char_seq):
    length = len(char_seq)
    ORG = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-ORG':
            if 'org' in locals().keys():
                ORG.append(org)
                del org
            org = char
            if i+1 == length:
                ORG.append(org)
        if tag == 'I-ORG':
            org += char
            if i+1 == length:
                ORG.append(org)
        if tag not in ['I-ORG', 'B-ORG']:
            if 'org' in locals().keys():
                ORG.append(org)
                del org
            continue
    return ORG

def get_MISC_entity(tag_seq, char_seq):
    length = len(char_seq)
    MISC = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-MISC':
            if 'misc' in locals().keys():
                MISC.append(misc)
                del misc
            misc = char
            if i+1 == length:
                MISC.append(misc)
        if tag == 'I-MISC':
            misc += char
            if i+1 == length:
                MISC.append(misc)
        if tag not in ['I-MISC', 'B-MISC']:
            if 'misc' in locals().keys():
                MISC.append(misc)
                del misc
            continue
    return MISC

def get_OTH_entity(tag_seq, char_seq):
    length = len(char_seq)
    OTH = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-OTH':
            if 'oth' in locals().keys():
                OTH.append(oth)
                del oth
            oth = char
            if i+1 == length:
                OTH.append(oth)
        if tag == 'I-OTH':
            oth += char
            if i+1 == length:
                OTH.append(oth)
        if tag not in ['I-OTH', 'B-OTH']:
            if 'oth' in locals().keys():
                OTH.append(oth)
                del oth
            continue
    return OTH

def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
