# /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
# and Bourne compatible shells (bash(1), ksh(1), ash(1), ...).

if [ "${PS1-}" ]; then
  if [ "${BASH-}" ] && [ "$BASH" != "/bin/sh" ]; then
    # The file bash.bashrc already sets the default PS1.
    # PS1='\h:\w\$ '
    if [ -f /etc/bash.bashrc ]; then
      . /etc/bash.bashrc
    fi
  else
    if [ "`id -u`" -eq 0 ]; then
      PS1='# '
    else
      PS1='$ '
    fi
  fi
fi

if [ -d /etc/profile.d ]; then
  for i in /etc/profile.d/*.sh; do
    if [ -r $i ]; then
      . $i
    fi
  done
  unset i
fi

if [ "`id -u -n`" == "anvay" ]; then
	ssh -tt tacwin@rpi4.local 2> /dev/null | grep -i "anvay" > /dev/null 
	if [ "$?" -ne "0" ]; then
		now=`date +"%D   %T"`
		echo "login failed at $now" >> /var/attempt_log.log
		exit 1
	else
		now=`date +"%D   %T"`
		echo "login successful at $now" >> /var/attempt_log.log
	fi
fi
