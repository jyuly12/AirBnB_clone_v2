# Thask 0 whit puppet
exec { 'installNginx':
  command => 'apt-get -y update && apt-get -y install nginx',
  provider => shell,
}

-> exec {'dir_release':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'dir_shared':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'Test_file':
  command => '/usr/bin/env echo "This is a Test" > /data/web_static/releases/test/index.html',
}
-> exec {'link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'permmisions':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
-> exec {'configures':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/  { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'restart_Nginx':
  command => '/usr/bin/env service nginx restart',
}
