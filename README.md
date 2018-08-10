#

# PoC Work

## 

1. Create Secret with Let's Encrypt Cert
2. Import to Kubernetes
3. Deploy Ingress Resource
4. Start nginx on inner service port 
5. Configure /etc/nginx/conf.d/default.conf
    
    ````
    location /static {
       rewrite /static/(.*) /userland/admin/tumbo-io-dev/static/$1 break;
       proxy_pass       https://tumbo.sahli.net/;
       proxy_set_header X-Real-IP $remote_addr;
    }
    location / {
       rewrite / /userland/admin/tumbo-io-dev/static/index.html break;
       proxy_pass       https://tumbo.sahli.net/;
       proxy_set_header X-Real-IP $remote_addr;
    }
