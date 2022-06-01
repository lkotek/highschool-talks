# Small demo for basic ansible usage

1. Install ansible itself:
sude dnf install ansible

2. Ensure your public ssh keys are on the managed servers:
ssh-copy-id root@managed.server

3. Create `/etc/ansible/hosts` file and fill with:
managed.server ansible_ssh_user=root

4. Prepare your playbook file (`certbot.yml`) by placing following content:
---
- hosts: managed.server
  user: root
  tasks:
  - name: Ensure certbot is installed
    dnf: 
      name: certbot 
      state: installed
  - name: Renew all web certifites
    ansible.builtin.command:
      cmd: certbot renew --non-interactive --agree-tos --dry-run
  - name: Restart nginx server
    ansible.builtin.service:
      name: nginx 
      state: restarted

5. Learn more using docs: https://docs.ansible.com/
