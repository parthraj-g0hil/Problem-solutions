import boto3# type: ignore
region = 'ap-south-1'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    
#1 ############# QA-OPL ############################   
    instance1 = ['i-01d2ea6ab73c739c2']
    ec2.stop_instances(InstanceIds=instance1);
    print('stoped your QA-OPL-enviroment')
    
#2 ############# SIT-OAM ###########################
    instance2 = ['i-0b0b5b83a9817cc2d']
    ec2.stop_instances(InstanceIds=instance2);
    print('stoped your SIT-OAM-enviroment')
    
#3 ############# QA-FITSgitCORE ############################   
    instance3 = ['i-0c6f9ce499b081e46']
    ec2.stop_instances(InstanceIds=instance3)
    print('stoped your QA-FITSCORE-enviroment')
    
#4 ############# RABBIT MQ ############################   
    instance4 = ['i-0a19bba1ae672e03f']
    ec2.stop_instances(InstanceIds=instance4)
    print('stoped your RABBIT MQ enviroment')
    
#5 ############# ANSIBLE SERVER ############################   
    instance5 = ['i-069985d6b534302af']
    ec2.stop_instances(InstanceIds=instance5)
    print('stoped your ANSIBLE enviroment')
    
    
#6 ############# GITLAB SERVER ############################   
    instance6 = ['i-094add32670167c44']
    ec2.stop_instances(InstanceIds=instance6)
    print('stoped your GITLAB enviroment')
    
#7 ############# Jenkins SERVER ############################   
    instance7 = ['i-0ab75c3f3494ad338']
    ec2.stop_instances(InstanceIds=instance7)
    print('stoped your Jenkins SERVER')
    
#8 ############# UAT_OPL SERVER ############################   
    instance8 = ['i-00aab5105e2bc5d34']
    ec2.stop_instances(InstanceIds=instance8)
    print('stoped your UAT_OPL enviroment')
    
#9 ############# PABL-SIT-SERVER ############################   
    instance11 = ['i-06cdf653255dc6746']
    ec2.stop_instances(InstanceIds=instance11)
    print('stoped your PABL-SIT-SERVER')
    
#10 ############# PABL-UAT-SERVER ############################   
    instance12 = ['i-05725e23687e6cdbd']
    ec2.stop_instances(InstanceIds=instance12)
    print('stoped your PABL-UAT-SERVER')
    
#11 ############ GUACAMOLE SERVER ############################   
    instance9 = ['i-0769d8c74a1313dfe']
    ec2.stop_instances(InstanceIds=instance9)
    print('stoped your UAT_OPL enviroment')

#12 ############# SIT-HSBC-APP-Server ###########################
    instance10 = ['i-0513967a98ee156d9']
    ec2.stop_instances(InstanceIds=instance10);
    print('stopped your SIT-HSBC-APP-Server')
    
    
#14 ############# GST-Jenkins SERVER ############################   
    instance14 = ['i-00508a44563fff7b8']
    ec2.stop_instances(InstanceIds=instance14)
    print('stoped your GST-Jenkins SERVER')
    
#15 ############# Ubuntu-RDP-For-Guacamole SERVER ############################   
    instance15 = ['i-0326ba09fffeb349e']
    ec2.stop_instances(InstanceIds=instance15)
    print('stoped your Ubuntu-RDP-For-Guacamole SERVER')
    
#16 ############# QA-PNBHL SERVER ############################   
    instance16 = ['i-0c88ad76309a476aa']
    ec2.stop_instances(InstanceIds=instance16)
    print('stoped your QA-PNBHL SERVER')
    
#17 ############# UAT-PNBHL SERVER ############################   
    instance17 = ['i-03b3fe82490e57011']
    ec2.stop_instances(InstanceIds=instance17)
    print('stoped your QA-PNBHL SERVER')
    
#18 ############# UAT-OAM SERVER ###########################
    instance18 = ['i-08bfe2726d14b9d9d']
    ec2.stop_instances(InstanceIds=instance18);
    print('stoped your UAT-OAM SERVER')

    
#20 ############# SIT-GST-SAHAY SERVER ############################   
    instance20 = ['i-013386b05a5f62b01']
    ec2.stop_instances(InstanceIds=instance20)
    print('stoped your SIT-GST-SAHAY SERVER')
    
#21 ############# QA-BOB-APP SERVER ############################   
    instance21 = ['i-07f3b0ac16b5ddb8d']
    ec2.stop_instances(InstanceIds=instance21)
    print('stoped your QA-BOB-APP SERVER' )
    
#22 ############# UAT-HSBC-APP-Server ###########################
    instance22 = ['i-08298fa1898851eb6']
    ec2.stop_instances(InstanceIds=instance22);
    print('stopped your UAT-HSBC-APP-Server')

#23 ############# UAT-HSBC-APP-NEW-Server ###########################
    instance23 = ['i-0c1d693472a4fd2bd']
    ec2.stop_instances(InstanceIds=instance23);
    print('started your UAT-HSBC-APP-NEW-Server')
    
#24 ############# Sonar-Server ###########################
    instance24 = ['i-0f00091a07cddc10c']
    ec2.stop_instances(InstanceIds=instance24);
    print('stopped your Sonar-Server')
    
#25 ############# QA-GST-SAHAY-Server ###########################
    instance25 = ['i-0443b0221966a1277']
    ec2.stop_instances(InstanceIds=instance25);
    print('stopped your QA-GST-SAHAY-Server')

#26 ############# PREPROD-BOB-APP-Server- ###########################
    instance26 = ['i-0f46d31c927065e7b']
    ec2.stop_instances(InstanceIds=instance26);
    print('stopped your PREPROD-BOB-APP-Server')

#27 ############# UAT-GST-SAHAY-Server ###########################
    instance27 = ['i-0db0edd13b5c49592']
    ec2.stop_instances(InstanceIds=instance27);
    print('stopped your UAT-GST-SAHAY-Server')

#28 ############# UAT-FITSCORE-APP-Server ###########################
    instance28 = ['i-0a31adf4f0822c68c']
    ec2.stop_instances(InstanceIds=instance28);
    print('stopped your UAT-FITSCORE-APP-Server')
    
#29 ############# UBI-UAT-GST-SAHAY-APP-SERVER ###########################
    instance29 = ['i-0307ef2d74fb22e05']
    ec2.stop_instances(InstanceIds=instance29);
    print('stopped your UBI-UAT-GST-SAHAY-APP-SERVER') 

#30 ############# PNB-UAT-GST-SAHAY-APP-SERVER ###########################
    instance30 = ['i-0579049fe0dd588ed']
    ec2.stop_instances(InstanceIds=instance30);
    print('stopped your PNB-UAT-GST-SAHAY-APP-SERVER')    
    
#31 ############# QA-PSB-HL-AL-APP-Server ###########################
    instance31 = ['i-0ef92d0087f7685aa']
    ec2.stop_instances(InstanceIds=instance31);
    print('stopped your QA-PSB-HL-AL-APP-Server')     

#32 #############JFROG_APP_Server ###########################
    instance32 = ['i-0d6cd90d4d9706057']
    ec2.stop_instances(InstanceIds=instance32);
    print('stopped your JFROG_APP_Server')  

#33 ############# MONGODBAPP_Server ###########################
    instance33 = ['i-01811951e3cd0950b']
    ec2.stop_instances(InstanceIds=instance33);
    print('stopped your MONGODBAPP_Server') 

#34 ############# QA-OAM_SERVER ###########################
    instance34 = ['i-034010ab5e8ec7a8c']
    ec2.stop_instances(InstanceIds=instance34);
    print('stopped your QA-OAM_SERVER') 

#25 ############# BOB-PSB-MIGRATION-Server ###########################
    instance35 = ['i-0cb300d763b9316f7']
    ec2.stop_instances(InstanceIds=instance35);
    print('started your BOB-PSB-MIGRATION-Server')

#36 ############# QA-HSBC-Server ###########################
    instance36 = ['i-00e78b4e070279bb4']
    ec2.stop_instances(InstanceIds=instance36);
    print('started your QA-HSBC-Server')