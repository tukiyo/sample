;#z::Run www.autohotkey.com

; * 
; + Shift
; ! Alt
; ^ control
; # win

; ���ϊ��L�[
sc07B::Send, !{Tab}
^sc07B::Send, ^{LButton}

sc073::Send, _

; �ϊ�
sc079::Send, {Right}
+sc079::Send, {Left}
^sc079::Send, {RButton}

; �J�^�J�i�A�Ђ炪��
sc070::Send, {Right}

;putty + vim
    !sc02B::Send, gt
    !sc01B::Send, gT
    ^sc00D::Send, :b +3{Enter};^

;
+WheelUp::Send, {PgUp}
+WheelDown::Send, {PgDn}

; Mac��Bootcamp�p�ݒ�
;sc15C::sc029

;; Happy Hacking �L�[�{�[�h�p
;Win+PgDn
#sc151::Send, #+{Down}
;Win+PgUp
#sc149::Send, #+{Up}
;Win+End
#sc14F::Send, #{Right}
;Win+Home
#sc147::Send, #{Left}