Controle de Gestos com Visão Computacional

Este projeto utiliza visão computacional para interpretar gestos manuais e transformá-los em comandos de teclado. Foi desenvolvido com Python, usando as bibliotecas OpenCV, MediaPipe e PyAutoGUI.

O objetivo é criar uma forma intuitiva de interagir com o computador, neste caso, para controlar a reprodução de mídias (pausar/continuar vídeos) com um simples movimento das mãos.

Funcionalidades
* Detecção de mãos e dedos em tempo real via webcam.
* Reconhecimento do número de dedos abertos para identificar gestos.
* Converte a mudança de gesto (mão fechada para aberta e vice-versa) em um comando de teclado ('k').
* Inclui um delay para evitar comandos acidentais.

Pré-requisitos
Para rodar o projeto, você precisará ter as seguintes bibliotecas instaladas:

* OpenCV
* MediaPipe
* PyAutoGUI

Você pode instalá-las usando o pip:

\``bash pip install opencv-python mediapipe pyautogui ```

Como executar
1.  Clone este repositório:
\``bash git clone https://github.com/Vn212/controle-de-gestos.git ```
2.  Navegue até o diretório do projeto:
\``bash cd controle-de-gestos ```
3.  Execute o script Python:
\``bash python gestos_controle.py ```
