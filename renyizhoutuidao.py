from manimlib.imports import *
import os
import pyclbr
'''
为解决三维向量箭头显示的问题，需修改这两个地方：
1.At geometry.py line 97 is the method position_tip(), right after the tip.rotate added:
    angle = angle_of_vector(handle - anchor) + PI/2
    a = np.array((np.cos(angle),np.sin(angle),0))
    tip.rotate(-phi_of_vector(handle - anchor),a)
2.a new method I defined in space_ops.py to calculate the phi angle of a vecter
def phi_of_vector(vector):
	xy = complex(*vector[:2])
	if xy == 0:
    	return 0;
	a = ((vector[:1])**2 + (vector[1:2])**2)**(1/2)
	vector[0] = a
	vector[1] = vector[2]
	return np.angle(complex(*vector[:2]))
'''
class SpinVectorViaAnyaxis(ThreeDScene,Scene):
	def construct(self):
		axes = ThreeDAxes()
		self.set_camera_orientation(phi=50 * DEGREES,theta=100*DEGREES,distance=6,gamma=0*DEGREES)
		direction_vector=2*1/np.sqrt(11)*(1*(UP)-1*(RIGHT)+3*(OUT))
		direction_vector_P=1*(UP)+2*(RIGHT)+2.5*(OUT) #任意向量P
		#vector_array_U=Vector(direction=(1*(UP)-1*(RIGHT)+3*(OUT))) #任意轴向量U
		#text1=TextMobject("任意轴向量U")  [-1,1,3]
		#vector_array_u=Vector(direction=1/np.sqrt(11)*(1*(UP)-1*(RIGHT)+3*(OUT))) #任意轴单位向量u
		vector_array_u=Vector(direction=direction_vector,color=BLUE_C) #任意轴单位向量u缩放两倍
		vector_array_P=Vector(direction=direction_vector_P)
		vector_array_P_CP=Vector(direction=direction_vector_P)
		#text2=TextMobject("任意轴单位向量U") #文字
		#print(vector_array_u)

		rx = 1/np.sqrt(11)*(-1)
		ry=1/np.sqrt(11)*1
		rz=1/np.sqrt(11)*3
		Theta=30*np.pi/180
		alpha=self.inv_triangle(ry/np.sqrt(ry*ry+rz*rz),rz/np.sqrt(ry*ry+rz*rz))
		beta=self.inv_triangle(rx,np.sqrt(ry*ry+rz*rz))
		#print("alpha=%.3f" % alpha,"beta=%.3f" % beta)
		'''
		text1.next_to(vector_array_U, RIGHT)
		text2.next_to(vector_array_u, RIGHT)
		'''
		matrix1 = self.matrix_xyz('X', alpha)
		matrix2 = self.matrix_xyz('Y', -1*beta)
		matrix3 = self.matrix_xyz('Z', Theta)
		matrix4 = self.matrix_xyz('Y', beta)
		matrix5 = self.matrix_xyz('X', -1*alpha)

		vector_dst1=np.dot(matrix1,direction_vector)
		vector_dst2=np.dot(matrix2,vector_dst1)
		vector_dst3=np.dot(matrix3,vector_dst2)
		vector_dst4=np.dot(matrix4,vector_dst3)
		vector_dst5=np.dot(matrix5,vector_dst4)
		vector_dst11=Vector(direction=vector_dst1,color=BLUE_C)
		vector_dst22=Vector(direction=vector_dst2,color=BLUE_C)
		vector_dst33=Vector(direction=vector_dst3,color=BLUE_C)
		vector_dst44=Vector(direction=vector_dst4,color=BLUE_C)
		vector_dst55=Vector(direction=vector_dst5,color=BLUE_C)

		vector_dst_P1=np.dot(matrix1,direction_vector_P)
		vector_dst_P2=np.dot(matrix2,vector_dst_P1)
		vector_dst_P3=np.dot(matrix3,vector_dst_P2)
		vector_dst_P4=np.dot(matrix4,vector_dst_P3)
		vector_dst_P5=np.dot(matrix5,vector_dst_P4)
		vector_dst_P=Vector(direction=np.dot(matrix5,vector_dst_P4),color=RED_C)
		vector_dst_P1=Vector(direction=vector_dst_P1)
		vector_dst_P2=Vector(direction=vector_dst_P2)
		vector_dst_P3=Vector(direction=vector_dst_P3)
		vector_dst_P4=Vector(direction=vector_dst_P4)
		vector_dst_P5=Vector(direction=vector_dst_P5)

		delay=1
		self.add(axes)
		#self.add(vector_array_U)
		#self.play(Write(text1),run_time = 2) #以书写的方式显示文字,运行时间为2s
		self.add(vector_array_u)
		self.add(vector_array_P)
		#self.play(Write(text2),run_time = 2) #以书写的方式显示文字,运行时间为2s
		#self.begin_ambient_camera_rotation(rate=1)
		self.wait(delay)
		#self.play(Restore(self.camera.frame))
		self.play(Transform(vector_array_P,vector_dst_P),run_time = delay)
		self.add(vector_dst_P)
		self.move_camera(phi=80 * DEGREES,theta=30*DEGREES,run_time=delay)
		self.add(vector_array_P_CP)
		self.wait(1)
		self.play(ReplacementTransform(vector_array_u,vector_dst11),ReplacementTransform(vector_array_P_CP,vector_dst_P1),run_time = delay)
		self.move_camera(theta=80*DEGREES,run_time=delay)
		self.play(ReplacementTransform(vector_dst11,vector_dst22),ReplacementTransform(vector_dst_P1,vector_dst_P2),run_time = delay)
		self.move_camera(phi=10 * DEGREES,theta=5*DEGREES,run_time=delay)
		self.play(ReplacementTransform(vector_dst22,vector_dst33),ReplacementTransform(vector_dst_P2,vector_dst_P3),run_time = delay)
		self.move_camera(phi=80 * DEGREES,theta=80*DEGREES,run_time=delay)
		self.play(ReplacementTransform(vector_dst33,vector_dst44),ReplacementTransform(vector_dst_P3,vector_dst_P4),run_time = delay)
		self.move_camera(phi=60 * DEGREES,theta=10*DEGREES,run_time=delay)
		self.play(ReplacementTransform(vector_dst44,vector_dst55),ReplacementTransform(vector_dst_P4,vector_dst_P5),run_time = delay)
		self.move_camera(phi=80 * DEGREES,theta=20*DEGREES,run_time=delay)
		'''
		self.add(vector_dst1)
		self.wait(2)
		self.add(vector_dst2)
		self.wait(2)
		self.add(vector_dst3)
		self.wait(2)
		self.add(vector_dst4)
		self.wait(2)
		self.add(vector_dst5)
		'''

		#self.apply_matrix(matrix)
		#self.add_title(TextGroup,animate=True)
		self.wait(delay)
		#self.stop_ambient_camera_rotation()

	def matrix_xyz(self,Axe_of_XYZ,angle):
		if Axe_of_XYZ=='X':
			Theta_X=angle
			matrix_X = [[1, 0, 0], [0, np.cos(Theta_X), -1*np.sin(Theta_X)], [0, np.sin(Theta_X), np.cos(Theta_X)]]
			return matrix_X
		if Axe_of_XYZ=='Y':
			Theta_Y=angle
			matrix_Y = [[np.cos(Theta_Y), 0,np.sin(Theta_Y)], [0, 1, 0], [-1*np.sin(Theta_Y), 0, np.cos(Theta_Y)]]
			return matrix_Y
		if Axe_of_XYZ=='Z':
			Theta_Z=angle
			matrix_Z = [[np.cos(Theta_Z), -1*np.sin(Theta_Z), 0], [np.sin(Theta_Z), np.cos(Theta_Z), 0], [0, 0, 1]]
			return matrix_Z
		
	def inv_triangle(self,sin_value=0, cos_value=1):
		sin_angle=np.arcsin(sin_value)
		cos_angle=np.arccos(cos_value)
		if(sin_angle>0):
			return cos_angle
		else:
			if(cos_angle>0):
				return sin_angle
			else:
				return cos_angle

class Renyizhougongshituidao(Scene):
    def construct(self):
        delay=2
        stc1=TextMobject("沿任意轴旋转及其推导")
        stc1.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        #stc2=TextMobject(r"\text{绕任意轴 } \vec{r} \text{旋转}",r"\theta",r"\text{角度的矩阵表示为R(}",r"\theta",r"\text{):}",font='songti')
        #stc2=TexMobject(r"\text{ The rotation matrix about any axis of the angle", r"\theta", r"\text{is R(", r"\theta",r"\text{):}")
        stc2=TexMobject(r"\text{The rotation matrix about any axis }",r"\vec{r}", r"\text{ of the angle } \theta \text{ is R(}",r"\theta",r"\text{):}")
        matrix_R_theta = TexMobject(r"\left[ {\begin{array}{*{20}{c}}r^2_x(1-cos\theta)+cos\theta &r_x r_y(1-cos\theta)-r_z sin\theta &r_x r_z(1-cos\theta)+r_y sin\theta\\r_x r_y(1-cos\theta)+r_z sin\theta &r^2_y(1-cos\theta)+cos\theta&r_y r_z(1-cos\theta)-r_x sin\theta \\  r_x r_z(1-cos\theta)-r_y sin\theta&r_y r_z(1-cos\theta)+r_x sin\theta &r^2_z(1-cos\theta)+cos\theta\end{array}} \right]").set_color(GOLD_A)
        matrix_R_theta.scale(0.7)

        self.play(Write(stc1))
        self.wait(delay)
        self.play(ApplyMethod(stc1.move_to,TOP+DOWN*2),run_time=delay)
        stc2.next_to(stc1,DOWN)
        self.play(Write(stc2))
        self.wait(delay)
        matrix_R_theta.next_to(stc2,2*DOWN)
        self.add(matrix_R_theta)
        self.wait(delay)
        sentence1=VGroup(stc1,stc2,matrix_R_theta)
        self.play(FadeOut(sentence1))

        stc3=TextMobject("沿任意轴旋转展示：").scale(1.2)
        self.play(Write(stc3))
        self.wait(delay)
        self.play(FadeOut(stc3))
        alpha=TexMobject(r"\alpha")
        alpha1=TexMobject(r"\alpha")
        beta=TexMobject(r"\beta")
        beta1=TexMobject(r"\beta")
        theta=TexMobject(r"\theta")
        tex1=TextMobject("（1）绕X轴转")
        tex2=TextMobject("（2）绕Y轴转-")
        tex3=TextMobject("（3）绕Z轴转")
        tex4=TextMobject("（4）绕Y轴转")
        tex5=TextMobject("（5）绕X轴转-")
        stc4=TextMobject("证明过程：").shift(UP*2.5+3*LEFT).scale(1.2).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        stc5=VGroup(tex1,alpha.next_to(tex1,RIGHT)).next_to(stc4,3.5*DOWN).align_to(stc4)
        stc6=VGroup(tex2,beta.next_to(tex2,RIGHT)).next_to(stc5,DOWN).align_to(stc4)
        stc7=VGroup(tex3,theta.next_to(tex3,RIGHT)).next_to(stc6,DOWN).align_to(stc4)
        stc8=VGroup(tex4,beta1.next_to(tex4,RIGHT)).next_to(stc7,DOWN).align_to(stc4)
        stc9=VGroup(tex5,alpha1.next_to(tex5,RIGHT)).next_to(stc8,DOWN).align_to(stc4)
        self.play(Write(stc4))
        self.add(stc5,stc6,stc7,stc8,stc9)
        self.wait(delay)

        #,r"\frac{r_y}{\sqrt{r_2_y+r_2_z}}"

        formula1=TexMobject(r"\text{sin}",r"\alpha",r"\text{=}",r"\frac{r_y}{\sqrt{r^2_y+r^2_z}}").shift(UP)
        formula2=TexMobject(r"\text{cos}",r"\alpha",r"\text{=}",r"\frac{r_z}{\sqrt{r^2_y+r^2_z}}").shift(0.5*DOWN)
        eq_group1=VGroup(formula1,formula2).shift(RIGHT*2+1.2*UP)
        braces=Brace(eq_group1,LEFT)
        self.play(GrowFromCenter(braces),Write(formula1),Write(formula2))
        formula3=TexMobject(r"\text{sin}",r"\beta",r"\text{=}",r"r_x").shift(0.5*DOWN).align_to(formula1)
        formula4=TexMobject(r"\text{cos}",r"\beta",r"\text{=}",r"\sqrt{r^2_y+r^2_z").shift(1.5*DOWN)
        eq_group2=VGroup(formula3,formula4).shift(RIGHT*2+0.8*DOWN)
        braces2=Brace(eq_group2,LEFT)
        self.play(GrowFromCenter(braces2),Write(formula3),Write(formula4))
        self.wait(delay)
        eq_group=VGroup(eq_group1,eq_group2)
        self.play(FadeOut(eq_group),FadeOut(braces),FadeOut(braces2),FadeOut(stc4),FadeOut(stc5),FadeOut(stc6),FadeOut(stc7),FadeOut(stc8),FadeOut(stc9))
        self.wait(delay)

        pre=TexMobject(r"\text{R(}",r"\theta",r"\text{)=}").move_to(6*LEFT)
        matrix_R_1 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}1&0&0\\0&cos\alpha&-sin\alpha\\0&sin\alpha &cos\alpha\end{array}} \right]\
            \left[ {\begin{array}{*{20}{c}}cos\beta&0&sin\beta\\0&1&0\\-sin\beta &0&cos\beta\end{array}} \right]\
            \left[ {\begin{array}{*{20}{c}}cos\theta&-sin\theta&0\\sin\theta &cos\theta&0\\0&0&1\end{array}} \right]\
            \left[ {\begin{array}{*{20}{c}}cos\beta&0&-sin\beta\\0&1&0\\sin\beta &0&cos\beta\end{array}} \right]\
            \left[ {\begin{array}{*{20}{c}}1&0&0\\0&cos\alpha&sin\alpha\\0&-sin\alpha &cos\alpha\end{array}} \right]\
            ").set_color(GOLD_A).scale(0.45).next_to(pre,RIGHT)
        self.add(pre,matrix_R_1)
        self.wait(delay)
        matrix_R_theta = TexMobject(r"\left[ {\begin{array}{*{20}{c}}r^2_x(1-cos\theta)+cos\theta &r_x r_y(1-cos\theta)-r_z sin\theta &r_x r_z(1-cos\theta)+r_y sin\theta\\r_x r_y(1-cos\theta)+r_z sin\theta &r^2_y(1-cos\theta)+cos\theta&r_y r_z(1-cos\theta)-r_x sin\theta \\  r_x r_z(1-cos\theta)-r_y sin\theta&r_y r_z(1-cos\theta)+r_x sin\theta &r^2_z(1-cos\theta)+cos\theta\end{array}} \right]").set_color(GOLD_A)
        matrix_R_theta.scale(0.6)
        matrix_R_theta.next_to(pre,RIGHT)
        self.play(Transform(matrix_R_1,matrix_R_theta))
        self.wait(delay)
        self.play(FadeOut(pre),FadeOut(matrix_R_1),FadeOut(matrix_R_theta))

        stc10=TextMobject("旋转证明过程展示：").scale(1.2)
        self.play(Write(stc10))
        self.wait(delay)


class kuaisuyanshi(Scene):
    def construct(self):
        delay=2
        stc1=TextMobject("快速演示：").scale(1.2)
        stc1.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        self.play(Write(stc1))
        self.wait(delay)