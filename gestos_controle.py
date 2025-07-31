import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Altere estes valores para definir um tamanho menor para a janela
largura_tela, altura_tela = 640, 480 # Sugestão de tamanho menor

COR_PRETA, COR_BRANCA = (0, 0, 0), (255, 255, 255)

prev_gesture = None
last_action_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    dedos = 0
    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if result.multi_handedness:
            hand_label = result.multi_handedness[0].classification[0].label 
            thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
            thumb_ip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x 
            if (hand_label == 'Right' and thumb_tip_x < thumb_ip_x) or \
               (hand_label == 'Left' and thumb_tip_x > thumb_ip_x):
                dedos += 1

        tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
        for tip in tips:
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                dedos += 1

        current_gesture = "fechado" if dedos == 0 else "aberto"
        if prev_gesture != current_gesture and time.time() - last_action_time > 1.5:
            pyautogui.press('k')
            prev_gesture = current_gesture
            last_action_time = time.time()

    frame_display = cv2.resize(frame, (largura_tela, altura_tela))
    cv2.putText(frame_display, f"Dedos: {dedos}", (50, 80), cv2.FONT_HERSHEY_DUPLEX, 2, COR_BRANCA, 4)
    cv2.putText(frame_display, f"Dedos: {dedos}", (50, 80), cv2.FONT_HERSHEY_DUPLEX, 2, COR_PRETA, 2)

    cv2.imshow("Controle de Gestos", frame_display)

    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()