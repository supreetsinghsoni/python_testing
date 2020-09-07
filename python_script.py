import git


class python_script:

    def push(self,git_repo):

    # Initializing git object

        repo = git.Repo()

    # Provide a list of the files to stage

        repo.index.add(['*'])

    # Provide a commit message

        repo.index.commit('Pushing via python code')

    # Push changes

        print (repo.remotes.origin.push())

    def clone(self,git_path, folder_path):
        git.Repo.clone_from(git_path, folder_path)

    def merge(self,files_list):

        data = ''

    # Reading data from file
        for file in files_list:
            with open(file) as fp:
                data += fp.read()
            data += "\n"
            data += "\n"


        with open('main_merged.tf', 'w') as fp:
            fp.write(data)


python_script = python_script()

#to merge files, call merge() and pass files as list in the sample format below
#python_script.merge(['main_subnet.tf','main_vpc.tf'])

#to push changes to an existing repo
python_script.push('python_testing')

#to clone a repo
#python_script.clone('https://github.com/supreetsinghsoni/python_testing.git', 'D:\python_git')

