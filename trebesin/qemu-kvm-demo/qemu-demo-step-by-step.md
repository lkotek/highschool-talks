# Small demo regarding qcow2 image and qemu-kvm

1. Install necessary tooling:
sudo dnf install guestfs-tools qemu-kvm

2. Download Fedora qcow2 image for generic cloud:
wget wget https://mirror.karneval.cz/pub/linux/fedora/linux/releases/36/Cloud/x86_64/images/Fedora-Cloud-Base-36-1.5.x86_64.qcow2

3. Rename to something more human readable:
mv Fedora-Cloud-Base-36-1.5.x86_64.qcow2 fedora.qcow2

4. Modify it and use root password:
virt-customize -a fedora.qcow2 --root-password password:linux

4. Run VM using qemu-kvm:
qemu-kvm -m 1024 -monitor stdio -qmp unix:./qmp-sock,server=on,wait=off fedora.qcow2

5. More docs here: https://qemu-project.gitlab.io/qemu/system/quickstart.html
