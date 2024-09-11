import boto3# type: ignore
region = 'ap-south-1'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    
#1 ############# QA-OPL ############################   
    instance1 = ['i-01d2ea6ab73c739c2']
    ec2.start_instances(InstanceIds=instance1);
    print('started your QA-OPL-enviroment')
    
#2 ############# SIT-OAM ###########################
    instance2 = ['i-0b0b5b83a9817cc2d']
    ec2.start_instances(InstanceIds=instance2);
    print('started your SIT-OAM-enviroment')
    
#3 ############# QA-FITSCORE ############################   
    instance3 = ['i-0c6f9ce499b081e46']
    ec2.start_instances(InstanceIds=instance3)
    print('started your QA-FITSCORE-enviroment')
    
#4 ############# RABBIT MQ ############################   
    instance4 = ['i-0a19bba1ae672e03f']
    ec2.start_instances(InstanceIds=instance4)
    print('started your RABBIT MQ enviroment')
    
#5 ############# ANSIBLE SERVER ############################   
    instance5 = ['i-069985d6b534302af']
    ec2.start_instances(InstanceIds=instance5)
    print('started your ANSIBLE enviroment')
    
    
#6 ############# GITLAB SERVER ############################   
    instance6 = ['i-094add32670167c44']
    ec2.start_instances(InstanceIds=instance6)
    print('started your GITLAB enviroment')
    
#7 ############# Jenkins SERVER ############################   
    instance7 = ['i-0ab75c3f3494ad338']
    ec2.start_instances(InstanceIds=instance7)
    print('started your GITLAB enviroment')
    
#8 ############# UAT_OPL SERVER ############################   
    instance8 = ['i-00aab5105e2bc5d34']
    ec2.start_instances(InstanceIds=instance8)
    print('started your UAT_OPL enviroment')
    
#9 ############# GUACAMOLE SERVER ############################   
    instance9 = ['i-0769d8c74a1313dfe']
    ec2.start_instances(InstanceIds=instance9)
    print('started your UAT_OPL enviroment')

#10 ############# SIT-HSBC-APP-Server ###########################
    instance10 = ['i-0513967a98ee156d9']
    ec2.start_instances(InstanceIds=instance10);
    print('started your SIT-HSBC-APP-Server')
    
#11 ############# SIT-PABL ###########################
    instance11 = ['i-06cdf653255dc6746']
    ec2.start_instances(InstanceIds=instance11);
    print('started your SIT-PABL-APP-Server')

#12 ############# UAT-PABL ###########################
    instance12 = ['i-05725e23687e6cdbd']
    ec2.start_instances(InstanceIds=instance12);
    print('started your UAT-PABL-APP-Server')
    
#13 ############# SIT-PAPQ ###########################
#    instance13 = ['i-0e3d600f73df0ed52']
#    ec2.start_instances(InstanceIds=instance13);
#    print('started your UAT-PABL-APP-Server')
    
#14 ############# GST-Jenkins SERVER ############################   
    instance14 = ['i-00508a44563fff7b8']
    ec2.start_instances(InstanceIds=instance14)
    print('started your GST-Jenkins SERVER')   
    
#15 ############# Ubuntu-RDP-For-Guacamole SERVER ############################   
    instance15 = ['i-0326ba09fffeb349e']
    ec2.start_instances(InstanceIds=instance15)
    print('started your Ubuntu-RDP-For-Guacamole SERVER')
    
#16 ############# QA-PNBHL SERVER ############################   
    instance16 = ['i-0c88ad76309a476aa']
    ec2.start_instances(InstanceIds=instance16)
    print('started your QA-PNBHL SERVER')
    
#17 ############# UAT-PNBHL SERVER ############################   
    instance17 = ['i-03b3fe82490e57011']
    ec2.start_instances(InstanceIds=instance17)
    print('started your QA-PNBHL SERVER')
    
#18 ############# UAT-OAM SERVER ###########################
    instance18 = ['i-08bfe2726d14b9d9d']
    ec2.start_instances(InstanceIds=instance18);
    print('started your UAT-OAM SERVER')
    
#19 ############# UAT-PAPQ ###########################
#    instance19 = ['i-0e6fd7301d601623c']
#    ec2.start_instances(InstanceIds=instance19);
#    print('started your UAT-PAPQ')
    
#20 ############# SIT-GST-SAHAY SERVER ############################   
    instance20 = ['i-013386b05a5f62b01']
    ec2.start_instances(InstanceIds=instance20)
    print('started your SIT-GST-SAHAY SERVER')

#21 ############# QA-BOB-APP SERVER ############################   
#    instance21 = ['i-07f3b0ac16b5ddb8d']
#    ec2.start_instances(InstanceIds=instance21)
#    print('started your QA-BOB-APP SERVER' )

#22 ############# UAT-HSBC-APP-Server ###########################
#    instance22 = ['i-08298fa1898851eb6']
#    ec2.start_instances(InstanceIds=instance22);
#    print('started your UAT-HSBC-APP-Server')

#23 ############# UAT-HSBC-APP-NEW-Server ###########################
    instance23 = ['i-0c1d693472a4fd2bd']
    ec2.start_instances(InstanceIds=instance23);
    print('started your UAT-HSBC-APP-NEW-Server')

#24 ############# Sonar-Server ###########################
    instance24 = ['i-0f00091a07cddc10c']
    ec2.start_instances(InstanceIds=instance24);
    print('started your Sonar-Server')
    
#25 ############# QA-GST-SAHAY-Server ###########################
    instance25 = ['i-0443b0221966a1277']
    ec2.start_instances(InstanceIds=instance25);
    print('started your QA-GST-SAHAY-Server')
    
#25 ############# PREPROD-BOB-APP-Server- ###########################
    instance26 = ['i-0f46d31c927065e7b']
    ec2.start_instances(InstanceIds=instance26);
    print('started your PREPROD-BOB-APP-Server')
    
#26 ############# UAT-GST-SAHAY-Server ###########################
    instance27 = ['i-0db0edd13b5c49592']
    ec2.start_instances(InstanceIds=instance27);
    print('started your UAT-GST-SAHAY-Server')

#27 ############# UAT-FITSCORE-APP-Server ###########################
    instance28 = ['i-0a31adf4f0822c68c']
    ec2.start_instances(InstanceIds=instance28);
    print('started your UAT-FITSCORE-APP-Server')
    
#28 ############# UBI-UAT-GST-SAHAY-APP-SERVER ###########################
    instance29 = ['i-0307ef2d74fb22e05']
    ec2.start_instances(InstanceIds=instance29);
    print('started your UBI-UAT-GST-SAHAY-APP-SERVER')

#29 ############# PNB-UAT-GST-SAHAY-APP-SERVER ###########################
    instance30 = ['i-0579049fe0dd588ed']
    ec2.start_instances(InstanceIds=instance30);
    print('started your PNB-UAT-GST-SAHAY-APP-SERVER') 
    
#30 ############# QA-PSB-HL-AL-APP-Server ###########################
    instance31 = ['i-0ef92d0087f7685aa']
    ec2.start_instances(InstanceIds=instance31);
    print('stopped your QA-PSB-HL-AL-APP-Server') 

#31 #############JFROG_APP_Server ###########################
    instance32 = ['i-0d6cd90d4d9706057']
    ec2.start_instances(InstanceIds=instance32);
    print('stopped your JFROG_APP_Server') 

#33 ############# MONGODBAPP_Server ###########################
    instance33 = ['i-01811951e3cd0950b']
    ec2.start_instances(InstanceIds=instance33);
    print('stopped your MONGODBAPP_Server') 
    
#34 ############# QA-OAM_SERVER ###########################
    instance34 = ['i-034010ab5e8ec7a8c']
    ec2.start_instances(InstanceIds=instance34);
    print('stopped your QA-OAM_SERVER') 

#35 ############# BOB-PSB-MIGRATION-Server ###########################
    instance35 = ['i-0cb300d763b9316f7']
    ec2.start_instances(InstanceIds=instance35);
    print('started your BOB-PSB-MIGRATION-Server')

#36 ############# QA-HSBC-Server ###########################
    instance36 = ['i-00e78b4e070279bb4']
    ec2.start_instances(InstanceIds=instance36);
    print('started your QA-HSBC-Server')