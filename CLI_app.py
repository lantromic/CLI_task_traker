import argparse
import json
import os

def load_tasks():
    if not os.path.exists('task_list.json'):
        with open('task_list.json','w') as f:
            json.dump([],f)
    with open('task_list.json','r') as f:
        try:
            data = json.load(f)
        except:
            data = None
            print("error accessing the file")
    return data

def output(args_params):
    data = load_tasks()
    if args_params == 'done':
         for dict in data:
            if dict['status'] == 'done':
                print('\n',dict['mission'],'\t','status: ',dict['status'],'\t','id: ',dict['id'])
    elif args_params == 'in-progress':
         for dict in data:
            if dict['status'] == 'in-progress':
                print('\n',dict['mission'],'\t','status: ',dict['status'],'\t','id: ',dict['id'])
    elif args_params == 'todo':
         for dict in data:
            if dict['status'] == 'todo':
                print('\n',dict['mission'],'\t','status: ',dict['status'],'\t','id: ',dict['id'])
    else:
        for i in data:
            print('\n',i['mission'],'\t','status: ',i['status'],'\t','id: ',i['id'])
    print('\n')

parser = argparse.ArgumentParser(description='haha')

parser.add_argument('command')
parser.add_argument('params',nargs='*')

args = parser.parse_args()

if args.command == 'add':
    id = 1 if load_tasks() == [] else max(load_tasks()[i]['id'] for i in range(0,len(load_tasks()))) + 1
    task_to_add= [{
    'mission': args.params[0],
    'status': 'todo',
    'id': id
    }]
    
    task = load_tasks()

    task = task + task_to_add

    with open('task_list.json','w') as f:
        json.dump(task,f)
    output('')
    print(f"\ntask added with id: {id}")

if args.command == 'update':
    id = int(args.params[0])
    data = load_tasks()
    try:
        task = {'mission': args.params[1], 'status': data[id-1]['status'], 'id': data[id-1]['id']}
        
        for dict in data:
            if dict['id'] == id:
                data[id-1] = task

        with open('task_list.json','w') as f:
            json.dump(data,f)

    except:
        print('make file in correct format first')
    output('')
    
if args.command == 'delete':
    id = int(args.params[0])
    data = load_tasks()

    try:
        for dict in data:
            if dict['id'] == id:
                data.pop(id-1)

        with open('task_list.json','w') as f:
            json.dump(data,f)

    except:
        print('make file in correct format first')
    output('')

if args.command == 'mark-in-progress':
    id = int(args.params[0])
    data = load_tasks()

    try:
        for dict in data:
            if dict['id'] == id:
                data[id-1]['status'] = 'in-progress'

        with open('task_list.json','w') as f:
            json.dump(data,f)

    except:
        print('make file in correct format first')
    output('')

if args.command == 'mark-done':
    id = int(args.params[0])
    data = load_tasks()

    try:
        for dict in data:
            if dict['id'] == id:
                data[id-1]['status'] = 'done'

        with open('task_list.json','w') as f:
            json.dump(data,f)

    except:
        print('make file in correct format first')
    output('')

if args.command == 'list':
    try:
        output(args.params[0])
    except:
        output(args.params)