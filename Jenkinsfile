pipeline(
   agent any

   stages{
      stage('Cloning Github repo to Jenkins'){
          steps{
              script{
                echo 'Cloning Github repo to jenkins.....................'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/sarthakshukla1856-debug/MLOPS-Course-project1.git']])
            }
        }
      }
   } 
)