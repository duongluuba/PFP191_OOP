from Student import Student
import math

class PFP191:
    # Hàm load file
    def load_file(self):
        list_sv = []
        try:
            with open('PFP191.txt','r') as file:
                for line in file:
                    code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t')
                    list_sv.append(Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
        except FileNotFoundError:
            file = open('PFP191.txt','w') 
            file.close()
        if list_sv == []:
            pass
        else:
            with open('PFP191.txt','w') as file :
                for st in list_sv:
                    file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')
        return list_sv
    # end def

    # hàm check code trong danh sách lớp:
    def check_code(self, code):
        list_sv = self.load_file()
        if list_sv == []:
            pass
        else:
            for st in list_sv:
                    if st.code == code:
                        return False
        return True
    # end def

    # hàm nhập thông tin sinh viên 
    def Input_Infor(self):
        # check code
        code = str(input('nhập mă số sinh viên:'))
        f = self.check_code(code)
        if f :
        # check name
            name = str(input('nhập tên học sinh:'))
            # check tuổi
            try:
                old = int(input('nhập tuổi:'))
            except:
                while True:
                    try:
                        old = int(input('nhập lại tuổi:'))
                        break
                    except:
                        continue
            # check lab
            try:
                lab = float(input('nhập điểm Lab:'))
            except:
                while True:
                    try:
                        lab = float(input('nhập lại điểm Lab:'))
                        break
                    except:
                        continue
            # check pt 
            try:
                pt = float(input('nhập điểm Practice:'))
            except:
                while True:
                    try:
                        pt = float(input('nhập lại điểm Practice:'))
                        break
                    except:
                        continue
            # check assignment
            try:
                assignment = float(input('nhập điểm Assignment:'))
            except:
                while True:
                    try:
                        assignment = float(input('nhập lại điểm Assignment:'))
                        break
                    except:
                        continue
            # check pe
            try:
                pe = float(input('nhập điểm Practice Exam:'))
            except:
                while True:
                    try:
                        pt = float(input('nhập lại điểm Practice Exam:'))
                        break
                    except:
                        continue
            # check fe
            try:
                fe = float(input('nhập điểm Final Exam:'))
            except:
                while True:
                    try:
                        fe = float(input('nhập lại điểm Final Exam:'))
                        break
                    except:
                        continue
            # tính điểm trung bình 
            avg = math.ceil( ((lab * 0.1) + (pt * 0.1) + (assignment * 0.2) + (pe * 0.3) + (fe * 0.3)) * 100) / 100

            # xếp loại học lực 
            if (avg >= 8):
                rank = "Gioi"
            elif (avg >= 6.5):
                rank = "Kha"
            elif (avg >= 5):
                rank = "Trung Binh"
            else:
                rank = "Yeu"      
            st = Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank)
            with open('PFP191.txt','a') as file :
                file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')
        else:
            print('Đã có mã sinh viên này trong lớp')
        # end def

    # hiển thị bảng điểm của lớp
    def Show_Infor(self):
        print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
              .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
        # hien thi danh sach sinh vien
        with open('PFP191.txt','r') as file:
            for line in file:
                    code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t')
                    print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}" 
                      .format(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
        print()
    

    # hàm cập nhập thông tin sinh viên
    def Update_student(self):
        code = str(input('nhập mă số sinh viên:'))
        with open("PFP191.txt", "r") as file:
            lines = file.readlines()
        found = False
        with open("PFP191.txt", "w") as file:
            for line in lines:
                student = line.strip().split('\t')
                if student[0] == code: # # nếu có student trong danh sách lớp
                    found = True
                    name = str(input('nhập tên học sinh:'))
                    # check tuổi
                    try:
                        old = int(input('nhập tuổi:'))
                    except:
                        while True:
                            try:
                                old = int(input('nhập lại tuổi:'))
                                break
                            except:
                                continue
                    # check lab
                    try:
                        lab = float(input('nhập điểm Lab:'))
                    except:
                        while True:
                            try:
                                lab = float(input('nhập lại điểm Lab:'))
                                break
                            except:
                                continue
                    # check pt 
                    try:
                        pt = float(input('nhập điểm Practice:'))
                    except:
                        while True:
                            try:
                                pt = float(input('nhập lại điểm Practice:'))
                                break
                            except:
                                continue
                    # check assignment
                    try:
                        assignment = float(input('nhập điểm Assignment:'))
                    except:
                        while True:
                            try:
                                assignment = float(input('nhập lại điểm Assignment:'))
                                break
                            except:
                                continue
                    # check pe
                    try:
                        pe = float(input('nhập điểm Practice Exam:'))
                    except:
                        while True:
                            try:
                                pt = float(input('nhập lại điểm Practice Exam:'))
                                break
                            except:
                                continue
                    # check fe
                    try:
                        fe = float(input('nhập điểm Final Exam:'))
                    except:
                        while True:
                            try:
                                fe = float(input('nhập lại điểm Final Exam:'))
                                break
                            except:
                                continue
                    # tính điểm trung bình 
                    avg = math.ceil( ((lab * 0.1) + (pt * 0.1) + (assignment * 0.2) + (pe * 0.3) + (fe * 0.3)) * 100) / 100
                    # xếp loại học lực 
                    if (avg >= 8):
                        rank = "Gioi"
                    elif (avg >= 6.5):
                        rank = "Kha"
                    elif (avg >= 5):
                        rank = "Trung Binh"
                    else:
                        rank = "Yeu"  
                    student[0] = code    
                    student[1] = name
                    student[2] = old
                    student[3] = lab
                    student[4] = pt
                    student[5] = assignment
                    student[6] = pe
                    student[7] = fe
                    student[8] = avg
                    student[9] = rank
                    file.write(f'{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]}\t{student[7]}\t{student[8]}\t{student[9]}\n')
                # end def
                    print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                        .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
                    print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                        .format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7], student[8], student[9]))
                    print("Student update successfully.") 
                else: 
                    file.write(line)
        if not found:# không có student trong danh sách lớp 
            print("Student not found.")
        print()
    # end def

    # Tìm kiếm sinh viên theo điểm Lab
    def search_by_point(self, name_point, point):
        Students = []
        with open('PFP191.txt', 'r') as file:
            for line in file:
                st = line.strip().split('\t')
                if float(st[int(name_point + 2)]) == point :
                    Students.append(Student(st[0], st[1], st[2], st[3], st[4], st[5], st[6], st[7], st[8], st[9]))
        print('Danh sách viên viên có điểm lab:',point)
        print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
            .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
        for student in Students:
            print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                .format(student.code, student.name, student.old, student.lab, student.pt, student.assignment, student.pe, student.fe, student.avg, student.rank))
        print()  
    # end def

    #  hàm đọc file
    def read_file(self):
        list_student = []
        with open('PFP191.txt','r') as file:
            for line in file:
               code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t') 
               list_student.append(Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
        return list_student
    # end def

    # hàm viết vào file 
    def write_file(self, list_student):
        with open('PFP191.txt','w') as file:
            for st in list_student:
                file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')
        file.close()
    # end def

    # sắp xếp theo tuổi nhưng không lưu dữ liệu sắp xếp vào file 
    def sort_by_old(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: int(x.old), reverse = True)
        print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
            .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
        for student in list_student:
            print("{:<14} | {:<16} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                .format(student.code, student.name, student.old, student.lab, student.pt, student.assignment, student.pe, student.fe, student.avg, student.rank))
    # end def

    # sắp xếp theo điểm lab và có lưu dữ liệu sắp xếp vào file 
    def sort_by_lab(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.lab), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm Practice
    def sort_by_pt(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.pt), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm Assignment
    def sort_by_assignment(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.assignment), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm PE
    def sort_by_pe(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.pe), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm PE
    def sort_by_fe(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.fe), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm trung bình 
    def sort_by_avg(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.avg), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def
    
    # hàm xóa student khỏi lớp bằng mã code
    def Delete_student_by_code(self):
        code = input("Enter code student id to delete: ")
        with open("PFP191.txt", "r") as file:
            lines = file.readlines()
        found = False
        with open("PFP191.txt", "w") as file:
            for line in lines:
                student = line.strip().split('\t')
                if student[0] != code:
                    file.write(line)
                else:
                    found = True
        if found:
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    # end def

    # xóa toàn bộ danh sách 
    def Delete_all(self):
        file = open('PFP191.txt','w') 
        file.close()



