import React from 'react';
import { View, TextInput, Button, Text } from 'react-native';

const Login = () => {
  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 24, marginBottom: 20 }}>Mobile Login</Text>
      <TextInput placeholder="Username" style={{ marginBottom: 10, borderWidth: 1, padding: 5 }} />
      <TextInput placeholder="Password" secureTextEntry style={{ marginBottom: 20, borderWidth: 1, padding: 5 }} />
      <Button title="Login" onPress={() => {}} />
    </View>
  );
};

export default Login;
