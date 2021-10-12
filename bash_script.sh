USERNAME="root"

declare -a hostnames=( "host1" "host2" "host3" )


PASSWORD="password123"

for host in ${hostnames[@]};
do
        ssh -p ${PASSWORD} -l ${USERNAME} ${host}

        echo " logged in to the host successfully ${host} "

        cd /tmp

        ls

        echo "deleting all logs in tmp folder"

        rm -rf *

        cmd=ls

        output=eval $cmd

        if [ $output ];

        then
                echo "some file couldn't delete"
                echo "these are the files ${check}"
        else
                echo "all files are deleted"

        fi

        echo "moving to /home folder"

        cd

        cd /home

        echo "deleting every thing from /home"

        rm -rf *

        cmd=ls

        output=eval $cmd

        if [ $output ];
        then
                echo "some file couldn't delete"
                echo "these are the files ${check}"
        else
                echo "all files are deleted"
        fi

done
