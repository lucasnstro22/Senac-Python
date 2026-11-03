with open("log.txt", "r", encoding="utf-8") as file:
    text = file.read().splitlines()
    email = ["admin@empresa.com",
             "root@empresa.com",
             "administrator@empresa.com",
             "secadmin@empresa.com",
             "sysadmin@empresa.com"]
print("="*20)
print("LOG DO SISTEMA")
print("="*20)
#---------------------------#
for acc in email:
        warn = 0
        info = 0
        error = 0
        ipArraw = []
        motivo = ""
        N_motivos = {} 
        for l in text:
            if acc in l:
                logItem = l.split(" ")

                #debug
                #print(f"LOG -- {logItem[6]}")
                #print(f"IDENTIFICADO - {acc} - {l}")

                if "ERROR" in l:
                    error = error + 1
                elif "INFO" in l:
                    info = info + 1
                elif "WARN" in l:
                    warn = warn + 1
                # print(logItem[6])
                
                ip = logItem[6].replace("ip=","")
                if ip not in ipArraw:
                        ipArraw.append(ip) 

                
                motivo = logItem[7]
                motivo = motivo.replace("reason=", "")
                if motivo in N_motivos:
                    N_motivos[motivo] += 1
                else:
                    N_motivos[motivo] = 1

        # Texto de IPv4s
        ipString = ""
        for ip in ipArraw: 
            ipString = ip + " - " + ipString
        ipString =  ipString[:-2]
        
        #Nível
        nv = ""
        nvN = 0

        #Definindo o maior número de tentativas
        if nvN < error:
            nv = "Error"
            nvN = error
        if nvN < info:
            nv = "INFO"
            nvN = info
        if nvN < warn:
            nv = "WARN"
            nvN = warn

        #Motivo com maior número de ocorrências
        motivoString = ""
        if motivo:
             motivoString = max(N_motivos, key=N_motivos.get)

        print(f"""
  Nível: {nv}
  Conta: {acc}
  IPs Suspeitos: {ipString}
  Contagem: {nvN}
  Motivo: {motivoString}
                """)
        print("-"*19)
#---------------------------#

print("="*20)
print("FIM DO LOG ")
print("="*20)

