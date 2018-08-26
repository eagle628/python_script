function y = generate_plant_response()
  s = tf('s');
  P = 1/(1+s);

  N = 1000;
  u = ones(N,1);
  Ts = 0.01;
  t = (0:Ts:Ts*(N-1))';
  y = lsim(P,u,t);
end
