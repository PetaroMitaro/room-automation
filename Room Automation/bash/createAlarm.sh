if [ -z $1 ];
then
  hr="*"
else
  hr=$1
fi

if [ -z $2 ];
then
  min="*"
else
  min=$2
fi
(crontab -l ; echo "$min $hr * * * ~/commands/alarm.sh") | sort - | uniq - | crontab -
