import serial;
import random, string;
while(1):
    ser = serial.Serial('COM4',9600);
        
    #FUN��O PEPE JA TIREI A VELA
    #SETA NA M�O, QUAL VAI INICIAR
    #DO1M - MOTOR ou DO1R - RODA
    
    valor = raw_input("Digite o valor: ");
    ser.write(valor+"\n");

    #TESTA O QUE DEU, E ATRIBUI A OBJETO O QUE �
    if(valor == "DO1M"):
        objeto = "Motor";
    else:
        objeto = "Roda";
        
    #PEGA A RESPOSTA DA PRIMEIRA ESTA��O   
    resposta = str(ser.read(3));
    print resposta
    if(resposta=="OK1"):
        arquivo = open('entrada.txt', 'a')
        objeto_mensagem = "ECHOESTA��O 1";
        arquivo.write('%s\n' % objeto_mensagem);
        arquivo.close()
        if(objeto == "Motor"):
            arquivo = open('entrada.txt', 'a')
            objeto_mensagem = "ECHOiniciar a produ��o do MOTOR";
            print ("iniciar a produ��o do MOTOR");
            arquivo.write('%s\n' % objeto_mensagem);
            arquivo.write('\n')
            arquivo.close()
            
        else:
            arquivo = open('entrada.txt', 'a')
            objeto_mensagem = "ECHOiniciar a produ��o da Roda";
            print ("iniciar a produ��o da Roda");
            arquivo.write('%s\n' % objeto_mensagem);
            arquivo.write('\n')
            arquivo.close()
            
        while(resposta != "DONE1OK"): #ENQUANTO A ESTA��O N�O ENCERRAR
            arquivo = open('entrada.txt', 'a')
            resposta = str(ser.read(90)); #COLETA AS ECHOS
            print resposta;
            ser.write("ECHOOK1\n");
            arquivo.write('%s\n' % resposta);
            arquivo.write('\n')
            arquivo.close()
                
            if(resposta == "DONE1"):#SE A REPOSTA FOR DONE1
                ser.write("DONE1OK\n");
                
            #TESTA QUAL � O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTA��O
            if(objeto == "Motor"):
                ser.write("DO2M\n")
            else:
               ser.write("DO2R\n")
               
            #PEGA A RESPOSTA DA SEGUNDA ESTA��O  
            resposta = str(ser.read(3));
            if(resposta=="OK2"):
                arquivo = open('entrada.txt', 'a')
                objeto_mensagem = "ECHOESTA��O 2";
                arquivo.write('%s\n' % objeto_mensagem);
                arquivo.close()
                if(objeto == "Motor"):
                    arquivo = open('entrada.txt', 'a')
                    objeto_mensagem = "ECHOInicia a uzinagem do MOTOR";
                    print ("Inicia a uzinagem do MOTOR");
                    arquivo.write('%s\n' % objeto_mensagem);
                    arquivo.write('\n')
                    arquivo.close()
                else:
                    arquivo = open('entrada.txt', 'a')
                    objeto_mensagem = "ECHOInicia a uzinagem da RODA";
                    print ("Inicia a uzinagem da RODA");
                    arquivo.write('%s\n' % objeto_mensagem);
                    arquivo.write('\n')
                    arquivo.close()
                    
                while(resposta != "DONE2"):#ENQUANTO A ESTA��O N�O ENCERRAR
                     arquivo = open('entrada.txt', 'a')
                     resposta = str(ser.read(90)); #COLETA AS ECHOS
                     print resposta;
                     ser.write("ECHOOK2\n");
                     arquivo.write('%s\n' % resposta);
                     arquivo.write('\n')
                     arquivo.close()
                    
                if(respota == "DONE2"):
                    ser.write("DONE2OK")#ENVIA UM DONE2OK
                    #TESTA QUAL � O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTA��O
                    if(objeto == "Motor"):
                        ser.write("DO3M\n")
                    else:
                        ser.write("DO3R\n")
                    #PEGA A RESPOSTA DA TERCEIRA ESTA��O      
                    resposta = str(ser.read(3));
                    if(resposta=="OK3"):
                        arquivo = open('entrada.txt', 'a')
                        objeto_mensagem = "ECHOESTA��O 3";
                        arquivo.write('%s\n' % objeto_mensagem);
                        arquivo.close()
                        if(objeto == "Motor"):
                            arquivo = open('entrada.txt', 'a')
                            objeto_mensagem = "ECHOPosiciona o bloco do MOTOR";
                            print ("Posiciona o bloco do MOTOR");
                            arquivo.write('%s\n' % objeto_mensagem);
                            arquivo.close()
                        else:
                            arquivo = open('entrada.txt', 'a')
                            objeto_mensagem = "ECHOPosiciona o pneu da RODA";
                            print ("Posiciona o pneu da RODA");
                            arquivo.write('%s\n' % objeto_mensagem);
                            arquivo.close()

                        while(resposta != "DONE3"):#ENQUANTO A ESTA��O N�O ENCERRAR
                             arquivo = open('entrada.txt', 'a')
                             resposta = str(ser.read(90)); #COLETA AS ECHOS
                             print resposta;
                             ser.write("ECHOOK3\n");
                             arquivo.write('%s\n' % resposta);
                             arquivo.write('\n')
                             arquivo.close()

                        if(respota == "DONE3"):#SE A REPOSTA FOR DONE3
                            ser.write("DONE3OK")#ENVIA UM DONE3OK
                            #TESTA QUAL � O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTA��O
                            if(objeto == "Motor"):
                                ser.write("DO4M\n")
                            else:
                                ser.write("DO4R\n")
                            #PEGA A RESPOSTA DA QUARTA ESTA��O             
                            resposta = str(ser.read(3));

                            if(resposta=="OK4"):
                                arquivo = open('entrada.txt', 'a')
                                objeto_mensagem = "ECHOESTA��O 4";
                                arquivo.write('%s\n' % objeto_mensagem);
                                arquivo.close()
                                if(objeto == "Motor"):
                                    arquivo = open('entrada.txt', 'a')
                                    objeto_mensagem = "ECHOInicia a montagem do MOTOR";
                                    print ("Inicia a montagem do MOTOR");
                                    arquivo.write('%s\n' % objeto_mensagem);
                                    arquivo.close()
                                else:
                                    arquivo = open('entrada.txt', 'a')
                                    objeto_mensagem = "ECHOInicia a montagem da RODA";
                                    print ("Inicia a montagem da RODA");
                                    arquivo.write('%s\n' % objeto_mensagem);
                                    arquivo.close()

                                while(resposta != "DONE4"):#ENQUANTO A ESTA��O N�O ENCERRAR
                                    arquivo = open('entrada.txt', 'a')
                                    resposta = str(ser.read(90)); #COLETA AS ECHOS
                                    print resposta;
                                    ser.write("ECHOOK4\n");
                                    arquivo.write('%s\n' % resposta);
                                    arquivo.write('\n')
                                    arquivo.close()

                                if(respota == "DONE4"):#SE A REPOSTA FOR DONE4
                                    ser.write("DONE4OK")#ENVIA UM DONE4OK
                                    #TESTA QUAL � O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTA��O
                                    if(objeto == "Motor"):
                                        ser.write("DO5M\n")
                                    else:
                                        ser.write("DO5R\n")
                                    #PEGA A RESPOSTA DA QUINTA ESTA��O             
                                    resposta = str(ser.read(3));
                                    if(resposta=="OK5"):
                                        arquivo = open('entrada.txt', 'a')
                                        objeto_mensagem = "ECHOESTA��O 5";
                                        arquivo.write('%s\n' % objeto_mensagem);
                                        arquivo.close()
                                        ser2 = serial.Serial('COM5',9600);
                                        if(objeto == "Motor"):
                                            arquivo = open('entrada.txt', 'a')
                                            objeto_mensagem = "ECHOInicia a montagem do MOTOR";
                                            print ("Inicia a montagem do MOTOR");
                                            arquivo.write('%s\n' % objeto_mensagem);
                                            arquivo.close()
                                        else:
                                            arquivo = open('entrada.txt', 'a')
                                            objeto_mensagem = "ECHOInicia a montagem da RODA";
                                            print ("Inicia a montagem da RODA");
                                            arquivo.write('%s\n' % objeto_mensagem);
                                            arquivo.close()

                                        while(resposta != "DONE5"):#ENQUANTO A ESTA��O N�O ENCERRAR
                                            arquivo = open('entrada.txt', 'a')
                                            resposta = str(ser2.read(90)); #COLETA AS ECHOS
                                            print resposta;
                                            ser2.write("ECHOOK5\n");
                                            arquivo.write('%s\n' % resposta);
                                            arquivo.write('\n')
                                            arquivo.close()

                                        if(respota == "DONE5"):#SE A REPOSTA FOR DONE4
                                            ser2.write("DONE5OK")#ENVIA UM DONE4OK
                                            arquivo = open('entrada.txt', 'a')
                                            objeto_mensagem = "ECHOPROCESSO FINALIZADO";
                                            arquivo.write('%s\n' % objeto_mensagem);
                                            arquivo.close()
                                            
                                    
                                                                                                    

    
    ser.close()
