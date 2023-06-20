def main():
    
    ##################################################
    #Comlete your code here
    #Use m_perc and f_perc for your results
    ##################################################
    
    
    num_males = int(input("Enter the number of males in the class: "))
    num_females = int(input("Enter the number of females in the class: "))

    total = int(num_males + num_females)

    m_perc = float(( num_males / total) * 100)
    f_perc = float(( num_females / total) * 100)

    print("The total number of students: \t\t", total)
    print(f'The number of males and females: \t {num_males} \t {num_females} ')
    print(f'The percentage of males and females: \t {m_perc: .2f}% \t {f_perc: .2f}% ')




    ########################################
    # Do not delete the return statement
    ########################################
    
    return m_perc, f_perc


if __name__ == '__main__':
    main()
