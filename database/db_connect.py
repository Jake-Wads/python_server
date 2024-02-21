from os import system
import env

system(f'mysql -u {env.user} -p{env.password} --host {env.host}')
