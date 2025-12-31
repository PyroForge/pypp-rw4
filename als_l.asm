; linux 64bit nasm ps this dose not need to be a nasm but I want to take a short break of python
section .bss
	; variables
	open_input resb 5
	code1 resb 1
	code2 resb 1
	home_input resb 5
section .data
	; constancet
	open: db "V0.1", 10, "Assembly line simulator", 10
	openlen: equ $ - open
	code1_w: db "code1 is enabled", 10
	code1_wlen: equ $ - code1_w
	code2_w: db "code2 is enablnd", 10
	code2_wlen: equ $ - code2_w
	code1_msg: db "c1"
	code2_msg: db "c2"
	home_msg: db "| Assembly line simulator |", 10, "| arm,cost,makes          |", 10, "| arm1 1 0.1          (1) |", 10 , "| Assembly line simulator |", 10
	home_msglen: equ $ - home_msg
	one: db "1"
	two: db "2"
section .text
	global_start
_start:
	; going to print the opening msg
	mov rax,1
	mov rdi,1
	mov rsi,open
	mov rdx,openlen
	syscall
	; geting the opening input
	mov rax,0
	mov rdi,0
	mov rsi,open_input
	mov rdx,5
	syscall
	; echoing the input
	mov rdx,rax
	mov rax,1
	mov rdi,1
	mov rsi,open_input
	syscall
	; checking if open_input == code1 or open_input == code2
	movzx eax, word [code1_msg]
	movzx ebx, word [open_input]
	cmp eax, ebx
	sete al
	mov [code1], al
	cmp byte [code1], 1
	je code1_start
	;
	movzx eax, word [code2_msg]
	movzx ebx, word [open_input]
	cmp eax, ebx
	sete al
	mov [code2], al
	cmp byte [code2], 1
	je code2_start
	;
	jmp home
code1_start:
	mov rax,1
	mov rdi,1
	mov rsi,code1_w
	mov rdx,code1_wlen
	syscall
	jmp home
code2_start:
	mov rax,1
	mov rdi,1
	mov rsi,code2_w
	mov rdx,code2_wlen
	syscall
	jmp home
home:
	mov rax,1
	mov rdi,1
	mov rsi,home_msg
	mov rdx,home_msglen
	syscall
	mov rax,0
	mov rdi,0
	mov rsi,home_input
	mov rdx,5
	syscall
	jmp exit
exit:
	; exiting
	mov rax, 60
	xor rdi, rdi
	syscall