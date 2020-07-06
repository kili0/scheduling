class PATIENT():
    def __init__(self):
        self.isFirst = True
        self.isConcerta = False
        self.prev_visit = -1


PATIENT_SIZE = 16
SERVICE_SIZE = 16    # 8 hours * 4 slots (15 min = 1 slot)
MAX_DAYS = 2
SLOT_SIZE = (SERVICE_SIZE * MAX_DAYS)


def getNextPatient(patients):
    for pid in range(PATIENT_SIZE):
        if (patients[pid].isFirst == True):
            return pid
            break
    else:
        min_ = 1000
        min_pid = 1000

        for pid in range(PATIENT_SIZE):
            if (patients[pid].prev_visit < min_pid):
                min_ = patients[pid].prev_visit
                min_pid = pid
        return min_pid


def main():
    patients = list(range(PATIENT_SIZE))
    slot = list(range(SLOT_SIZE))

    for i in range(SLOT_SIZE):
        slot[i] = -1

    for i in range(PATIENT_SIZE):
        patients[i] = PATIENT()

    sid = 0
    while sid < SERVICE_SIZE:
        pid = getNextPatient(patients)

        if (patients[pid].isFirst == True):
            patients[pid].isFirst = False

            for i in range(3):
                slot[sid] = pid
                sid+=1
        else:
            slot[sid] = pid
            sid+=1

        patients[pid].prev_visit = sid

    result = list()
    for i in range(SLOT_SIZE):
        result.append(slot[i])
    print(result)


main()
