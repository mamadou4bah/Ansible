#!/usr/bin/python
# -*- coding: utf-8 -*-

# un module qui permet de décrire un personnage de jeux vidéo

from ansible.module_utils.basic import *

def presentation(module):
	name = module.params['name']
	attack = module.params['attack']
	inventory = module.params['inventory']
	return {"Presentation" : "My name is {} and my type of attack is {}, here is what you will find in my inventory : {}".format(name, attack, inventory)}

def main():
	fields = {
		"name": {"default" : "unknown", "type": "str"},
        "attack": {
        	"default": "melee", 
        	"choices": ['melee', 'distance'], 
        	"type": 'str'
        },
		"inventory": {"default": [], "required": False, "type": "list"},
	}
	module = AnsibleModule(argument_spec=fields)
	module.exit_json(changed=False, meta=presentation(module))


if __name__ == '__main__':
    main()