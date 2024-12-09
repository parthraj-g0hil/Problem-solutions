#!/bin/bash

echo "Starting vsftpd installation and configuration..."

# Step 1: Check OS and Install vsftpd
if [ -f /etc/debian_version ]; then
    echo "Detected Ubuntu/Debian. Installing vsftpd..."
    sudo apt update
    sudo apt install vsftpd -y
else
    echo "Detected RHEL/CentOS. Installing vsftpd..."
    sudo yum install vsftpd -y
fi

# Step 2: Backup existing vsftpd.conf
echo "Backing up vsftpd configuration file..."
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.bkp

# Step 3: Configure User
read -p "Enter the username for vsftpd: " username
if id "$username" &>/dev/null; then
    echo "User $username already exists. Proceeding..."
else
    echo "User $username does not exist. Creating..."
    sudo useradd -m -d /home/$username $username
    echo "Set password for the new user $username:"
    sudo passwd $username
fi

# Step 4: Set Default Directory
read -p "Do you want to set a custom default directory for the user? (yes/no): " set_dir
if [[ "$set_dir" == "yes" ]]; then
    read -p "Enter the path for the default directory: " user_path
    sudo mkdir -p $user_path
    sudo chown $username:$username $user_path
    sudo usermod -d $user_path -s /bin/bash $username
    echo "Default directory for $username set to $user_path."
fi

# Step 5: Create /etc/vsftpd.chroot_list
echo "Adding user $username to /etc/vsftpd.chroot_list..."
sudo bash -c "echo $username >> /etc/vsftpd.chroot_list"

# Step 6: Create /etc/vsftpd.userlist
echo "Adding user $username to /etc/vsftpd.userlist..."
sudo bash -c "echo $username >> /etc/vsftpd.userlist"

# Step 7: Get Public IP
echo "Fetching public IP..."
public_ip=$(curl -s ifconfig.me)
echo "Public IP: $public_ip"

# Step 8: Update vsftpd.conf
echo "Updating vsftpd configuration..."
sudo bash -c "cat > /etc/vsftpd.conf <<EOL
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
listen=YES
listen_ipv6=NO
pam_service_name=vsftpd
userlist_enable=YES
userlist_deny=NO
tcp_wrappers=YES
chroot_local_user=YES
chroot_list_enable=YES
pasv_promiscuous=YES
pasv_max_port=13100
pasv_min_port=13000
userlist_file=/etc/vsftpd.userlist
chroot_list_file=/etc/vsftpd.chroot_list
pasv_address=$public_ip
EOL"

# Step 9: Enable and Start vsftpd
echo "Enabling and starting vsftpd service..."
sudo systemctl enable vsftpd.service
sudo systemctl start vsftpd.service
sudo systemctl restart vsftpd.service 

echo "vsftpd installation and configuration completed successfully."

