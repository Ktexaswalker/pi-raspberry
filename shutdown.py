Importar  RPI . GPIO  como  GPIO
tiempo de importación
importar os

GPIO .setmode ( GPIO , BCM )
GPIO .setup ( 21 , GPIO . IN , pull_up_down = GPIO . PUD_UP )

def  apagado ( canal ):
  os.system ( " sudo shutdown -h now " )

GPIO .add_event_detext ( 21 , GPIO . FALLING , callback = shutdown, bouncetime = 1000 )

mientras que  1 :
  time.sleep ( 1 )
