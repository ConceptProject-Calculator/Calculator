#omnia task

#for clear and  + = - * and so on
btnClear = Button(calc, text="clear",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold')
                  ,bd=4, command=added_value.Clear_Entry).grid(row=1, column= 0, pady = 1)

btnAllClear = Button(calc, text="CE",width=6, height=2,bg='#581845',fg='white', font=('Helvetica'
            ,20,'bold'),bd=4,command=added_value.All_Clear_Entry).grid(row=1, column= 1, pady = 1)

btnsq = Button(calc, text="\u221A",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.squared).grid(row=1, column= 2, pady = 1)
btnAdd = Button(calc, text="+",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.operation("add")
                ).grid(row=1, column= 3, pady = 1)

btnSub = Button(calc, text="-",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.operation("sub")
                ).grid(row=2, column= 3, pady = 1)

btnMul = Button(calc, text="x",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                 bd=4,command=lambda:added_value.operation("multi")
                ).grid(row=3, column= 3, pady = 1)

btnDiv = Button(calc, text="/",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                 bd=4,command=lambda:added_value.operation("divide")
                ).grid(row=4, column= 3, pady = 1)

btnZero = Button(calc, text="0",width=6, height=2,bg='#581845',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.numberEnter(0)
                 ).grid(row=5, column= 0, pady = 1)

btnDot = Button(calc, text=".",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.numberEnter(".")
                ).grid(row=5, column= 1, pady = 1)
btnPM = Button(calc, text=chr(177),width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.mathPM).grid(row=5, column= 2, pady = 1)

btnEquals = Button(calc, text="=",width=6, height=2,bg='#581845',fg='white', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.sum_of_total).grid(row=5, column= 3, pady = 1)
